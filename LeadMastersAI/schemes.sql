from pydantic import BaseModel, EmailStr
from typing import List, Optional

class RegisterIn(BaseModel):
    email: EmailStr
    password: str

class LoginIn(BaseModel):
    email: EmailStr
    password: str

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"

class QuestionOut(BaseModel):
    id: int
    text: str
    options: List[dict]

class StartExamOut(BaseModel):
    exam_id: int
    end_epoch: int
    questions: List[QuestionOut]

class SubmitIn(BaseModel):
    exam_id: int
    answers: List[dict]  # [{question_id, option_id}]
