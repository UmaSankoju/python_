import { startExam } from "../api";

export default function Start() {
  const go = async () => {
    const data = await startExam();
    sessionStorage.setItem("exam", JSON.stringify(data));
    window.location.href = "/exam";
  };
  return (
    <div style={{maxWidth:480, margin:"40px auto", textAlign:"center"}}>
      <h2>Start Exam</h2>
      <p>Duration: 30 minutes • 10 questions • MCQs</p>
      <button onClick={go}>Start</button>
    </div>
  );
}
