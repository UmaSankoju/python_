import { useState } from "react";
import { login } from "../api";

export default function Login() {
  const [email,setEmail]=useState(""); const [password,setPassword]=useState(""); const [err,setErr]=useState("");
  const submit = async (e) => {
    e.preventDefault();
    try { await login(email, password); window.location.href="/start"; }
    catch (e) { setErr("Invalid credentials"); }
  };
  return (
    <form onSubmit={submit} style={{maxWidth:360, margin:"48px auto"}}>
      <h2>Login</h2>
      <input placeholder="Email" value={email} onChange={e=>setEmail(e.target.value)} required />
      <input placeholder="Password" type="password" value={password} onChange={e=>setPassword(e.target.value)} required />
      <button>Login</button>
      {err && <p style={{color:"red"}}>{err}</p>}
    </form>
  );
}
