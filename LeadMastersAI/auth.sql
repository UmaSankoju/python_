import os, time, jwt
from passlib.hash import bcrypt

SECRET = os.getenv("JWT_SECRET", "devsecret")
ALGO = "HS256"
TTL = 60 * 60 * 24

def hash_pw(p): return bcrypt.hash(p)
def verify_pw(p, h): return bcrypt.verify(p, h)

def make_token(user_id: int):
    payload = {"sub": str(user_id), "iat": int(time.time()), "exp": int(time.time()) + TTL}
    return jwt.encode(payload, SECRET, algorithm=ALGO)

def parse_token(token: str) -> int:
    data = jwt.decode(token, SECRET, algorithms=[ALGO])
    return int(data["sub"])
