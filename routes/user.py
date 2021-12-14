from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

from jose import jwt
from starlette import status
from funciones.funciones_user import get_password_hash, verify_password, create_access_token, get_current_active_user
from schemas.user import NewUser, User
from models.user import TablaUser
from config.hogwarts_BD import conexion

SECRET_KEY = "4c52095afed2de089cd131047620628a40f7babf2ec502ee7e12a706fc44ff7d"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120

user = APIRouter()


@user.post("/registro")
def create_user(new_user: NewUser):
    new_user = {
        "username": new_user.username,
        "password": get_password_hash(new_user.password)
    }
    resultado = conexion.execute(TablaUser.insert().values(new_user))
    return conexion.execute(TablaUser.select().where(TablaUser.c.id == resultado.lastrowid)).first()

@user.post("/login")
def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    loginUsername = form_data.username
    loginPassword = form_data.password
    usuario = conexion.execute(TablaUser.select().where(
        TablaUser.c.username == loginUsername)).first()

    if not usuario or not verify_password(loginPassword, usuario.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": usuario.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer", "user": usuario}

@user.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@user.get("/login/{username}")
def get_usuario(username: str):
    return conexion.execute(TablaUser.select().where(TablaUser.c.username == username)).first()
