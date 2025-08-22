import { useEffect, useState } from "react";

export default function useCountdown(endEpoch, onExpire) {
  const [left, setLeft] = useState(() => Math.max(0, endEpoch - Math.floor(Date.now()/1000)));
  useEffect(() => {
    const t = setInterval(() => {
      const sec = Math.max(0, endEpoch - Math.floor(Date.now()/1000));
      setLeft(sec);
      if (sec === 0) { clearInterval(t); onExpire?.(); }
    }, 1000);
    return () => clearInterval(t);
  }, [endEpoch, onExpire]);
  return left; // seconds left
}
