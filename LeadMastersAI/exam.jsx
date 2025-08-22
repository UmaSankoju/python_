import { useEffect, useMemo, useState } from "react";
import useCountdown from "../hooks/useCountdown";
import { submitExam } from "../api";

export default function Exam() {
  const saved = JSON.parse(sessionStorage.getItem("exam") || "{}");
  const { exam_id, end_epoch, questions=[] } = saved;

  const [idx, setIdx] = useState(0);
  const [answers, setAnswers] = useState({}); // qid -> option_id
  const secondsLeft = useCountdown(end_epoch, () => doSubmit());

  const q = questions[idx];

  const doSubmit = async () => {
    const payload = Object.entries(answers).map(([qid, oid]) => ({ question_id: +qid, option_id: +oid }));
    const res = await submitExam(exam_id, payload);
    sessionStorage.removeItem("exam");
    window.location.href = `/result/${exam_id}?score=${res.score}`;
  };

  useEffect(() => {
    if (!exam_id) window.location.href="/start";
  }, [exam_id]);

  const mmss = useMemo(() => {
    const m = Math.floor(secondsLeft/60), s = secondsLeft%60;
    return `${m.toString().padStart(2,"0")}:${s.toString().padStart(2,"0")}`;
  }, [secondsLeft]);

  if (!q) return null;

  return (
    <div style={{maxWidth:720, margin:"24px auto"}}>
      <div style={{display:"flex", justifyContent:"space-between", alignItems:"center"}}>
        <h3>Question {idx+1} / {questions.length}</h3>
        <div><strong>⏱ {mmss}</strong></div>
      </div>
      <p style={{fontSize:18}}>{q.text}</p>
      <div>
        {q.options.map(o => (
          <label key={o.id} style={{display:"block", margin:"8px 0"}}>
            <input
              type="radio"
              name={`q-${q.id}`}
              checked={answers[q.id] === o.id}
              onChange={() => setAnswers(a => ({...a, [q.id]: o.id}))}
            />{" "}{o.text}
          </label>
        ))}
      </div>
      <div style={{marginTop:16, display:"flex", gap:8}}>
        <button disabled={idx===0} onClick={()=>setIdx(i=>i-1)}>Previous</button>
        <button disabled={idx===questions.length-1} onClick={()=>setIdx(i=>i+1)}>Next</button>
        <button style={{marginLeft:"auto"}} onClick={doSubmit}>Submit</button>
      </div>
    </div>
  );
}
