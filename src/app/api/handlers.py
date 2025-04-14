from fastapi import APIRouter
from src.app.api.models import UserCreate, ShowUser
from src.app.database.session import async_session
from src.app.database.user_service import UserService

user_router = APIRouter()


async def _create_new_user(user: UserCreate) -> ShowUser:
    async with async_session() as session:
        async with session.begin():
            user_service = UserService(session)
            user = await user_service.create_user(
                name=user.name,
                surname=user.surname,
                email=user.email,
            )
            return ShowUser(
                user_id=user.user_id,
                name=user.name,
                surname=user.surname,
                email=user.email
            )


@user_router.post("/", response_model=ShowUser)
async def create_user(body: UserCreate) -> ShowUser:
    return await _create_new_user(body)
