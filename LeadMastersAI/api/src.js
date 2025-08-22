const API = import.meta.env.VITE_API || "http://localhost:8000";

export const setToken = (t) => localStorage.setItem("token", t);
export const getToken = () => localStorage.getItem("token");

const headers = () => ({
  "Content-Type": "application/json",
  ...(getToken() ? { Authorization: `Bearer ${getToken()}` } : {})
});

export const register = async (email, password) => {
  const r = await fetch(`${API}/auth/register`, {
    method: "POST", headers: headers(), body: JSON.stringify({ email, password })
  });
  if (!r.ok) throw new Error(await r.text());
  const data = await r.json(); setToken(data.access_token); return data;
};

export const login = async (email, password) => {
  const r = await fetch(`${API}/auth/login`, {
    method: "POST", headers: headers(), body: JSON.stringify({ email, password })
  });
  if (!r.ok) throw new Error(await r.text());
  const data = await r.json(); setToken(data.access_token); return data;
};

export const startExam = async () => {
  const r = await fetch(`${API}/exam/start`, { method: "POST", headers: headers() });
  if (!r.ok) throw new Error(await r.text()); return r.json();
};

export const submitExam = async (exam_id, answers) => {
  const r = await fetch(`${API}/exam/submit`, {
    method: "POST", headers: headers(), body: JSON.stringify({ exam_id, answers })
  });
  if (!r.ok) throw new Error(await r.text()); return r.json();
};

export const getResult = async (exam_id) => {
  const r = await fetch(`${API}/exam/result/${exam_id}`, { headers: headers() });
  if (!r.ok) throw new Error(await r.text()); return r.json();
};
