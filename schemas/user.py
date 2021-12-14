from typing import Optional

from pydantic import BaseModel

class User(BaseModel):
    username: str
    is_active: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

class NewUser(User):
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
