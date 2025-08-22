from .database import Base, engine, SessionLocal
from .models import Question, Option

def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    if db.query(Question).count() > 0:
        print("Already seeded"); return
    samples = [
        ("What is 2 + 2?", [("3", False), ("4", True), ("5", False), ("22", False)]),
        ("Capital of India?", [("Mumbai", False), ("New Delhi", True), ("Kolkata", False), ("Chennai", False)]),
        # add more…
    ]
    for text, opts in samples:
        q = Question(text=text); db.add(q); db.flush()
        for t, ok in opts:
            db.add(Option(question_id=q.id, text=t, is_correct=ok))
    db.commit(); db.close(); print("Seeded.")

if __name__ == "__main__":
    seed()
