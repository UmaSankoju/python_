import { useParams, useSearchParams } from "react-router-dom";

export default function Result() {
  const { id } = useParams();
  const [sp] = useSearchParams();
  const score = sp.get("score");
  return (
    <div style={{textAlign:"center", margin:"60px auto"}}>
      <h2>Exam Result</h2>
      <p>Exam ID: {id}</p>
      <h1>Score: {score}</h1>
      <a href="/start">Take Again</a>
    </div>
  );
}
