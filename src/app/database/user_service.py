import uuid
from typing import Type, Any

from sqlalchemy import select, Result, CursorResult
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.database.models import User

DEFAULT_ROLE = "courier"


class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    # async def get_role_by_name(self, name: str) -> int:
    #     result = await self.db.execute(select(Role.id).where(Role.name == name))
    #     return result
    #
    # async def create_role(self, name: str) -> Role:
    #     role = Role(name=name)
    #     self.db.add(role)
    #     await self.db.flush()
    #     return role

    async def create_user(self, name: str, surname: str, email: str) -> User:
        user = User(
            name=name,
            surname=surname,
            email=email
        )
        self.db.add(user)
        await self.db.flush()
        return user

    # async def change_user_role(self, user_id: uuid.UUID, new_role_name: str):
    #     user = await self.db.get(User, user_id)
    #     if not user:
    #         raise ValueError("User not found")
    #
    #     role = await self.get_role_by_name(new_role_name)
    #     if not role:
    #         raise ValueError("Role not found")
    #
    #     user.role = role
    #     await self.db.commit()
    #     await self.db.refresh(user)
