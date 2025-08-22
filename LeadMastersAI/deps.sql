from fastapi import Depends, HTTPException, Header
from .auth import parse_token

def get_current_user_id(authorization: str = Header(None)):
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="Missing token")
    token = authorization.split(" ", 1)[1]
    try:
        return parse_token(token)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
