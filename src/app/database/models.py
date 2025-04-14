import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(AsyncAttrs, DeclarativeBase):
    pass


# class Role(Base):
#     __tablename__ = "roles"
#
#     id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
#     name: Mapped[str] = mapped_column(unique=True)


class User(Base):
    __tablename__ = 'users'

    user_id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)


# class Order(Base):
#     __tablename__ = 'orders'
