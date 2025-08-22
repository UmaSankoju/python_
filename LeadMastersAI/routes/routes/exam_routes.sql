import time, random
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Question, Option, Exam
from ..schemas import StartExamOut, SubmitIn
from ..deps import get_current_user_id

router = APIRouter(prefix="/exam", tags=["exam"])

@router.post("/start", response_model=StartExamOut)
def start_exam(db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    duration = 30 * 60
    start = int(time.time())
    exam = Exam(user_id=user_id, duration_seconds=duration, started_at_epoch=start)
    db.add(exam); db.commit(); db.refresh(exam)

    q_ids = [q.id for q in db.query(Question).all()]
    if len(q_ids) < 10:
        raise HTTPException(500, "Not enough questions")
    chosen = random.sample(q_ids, 10)
    questions = db.query(Question).filter(Question.id.in_(chosen)).all()

    out = []
    for q in questions:
        opts = db.query(Option).filter(Option.question_id == q.id).all()
        out.append({
            "id": q.id,
            "text": q.text,
            "options": [{"id": o.id, "text": o.text} for o in opts]  # no correctness exposed
        })

    return {"exam_id": exam.id, "end_epoch": start + duration, "questions": out}

@router.post("/submit")
def submit_exam(payload: SubmitIn, db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    exam = db.query(Exam).filter(Exam.id == payload.exam_id, Exam.user_id == user_id).first()
    if not exam:
        raise HTTPException(404, "Exam not found")
    if exam.ended:
        return {"score": exam.score}

    # server-side cutoff
    now = int(time.time())
    cutoff = exam.started_at_epoch + exam.duration_seconds
    if now > cutoff:
        # continue; still score and mark ended
        pass

    score = 0
    for a in payload.answers:
        qid, oid = a.get("question_id"), a.get("option_id")
        if not (qid and oid): continue
        opt = db.query(Option).filter(Option.id == oid, Option.question_id == qid).first()
        if opt and opt.is_correct:
            score += 1

    exam.score = score
    exam.ended = True
    db.commit()
    return {"score": score}

@router.get("/result/{exam_id}")
def get_result(exam_id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    exam = db.query(Exam).filter(Exam.id == exam_id, Exam.user_id == user_id).first()
    if not exam:
        raise HTTPException(404, "Exam not found")
    return {"exam_id": exam.id, "score": exam.score, "ended": exam.ended, "duration": exam.duration_seconds}
