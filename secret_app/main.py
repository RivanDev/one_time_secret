from fastapi import FastAPI
from fastapi_users import fastapi_users, FastAPIUsers

from secret_app.auth.auth import auth_backend
from secret_app.auth.database import User
from secret_app.auth.manager import get_user_manager
from secret_app.auth.schemas import UserRead, UserCreate

app = FastAPI(
    title="One time secret"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


@app.get("/")
def root():
    return {"message": "Hello! It's one time secret service"}
