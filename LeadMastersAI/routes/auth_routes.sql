from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User
from ..schemas import RegisterIn, LoginIn, TokenOut
from ..auth import hash_pw, verify_pw, make_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=TokenOut)
def register(payload: RegisterIn, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(status_code=400, detail="Email exists")
    user = User(email=payload.email, password_hash=hash_pw(payload.password))
    db.add(user); db.commit(); db.refresh(user)
    return {"access_token": make_token(user.id)}

@router.post("/login", response_model=TokenOut)
def login(payload: LoginIn, db: Session = Depends(get_db)):
    u = db.query(User).filter(User.email == payload.email).first()
    if not u or not verify_pw(payload.password, u.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": make_token(u.id)}
