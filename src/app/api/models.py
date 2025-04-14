import re
import uuid

from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, field_validator

LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")


class TunedModel(BaseModel):
    class Config:
        """tells pydantic to convert even non dict obj to json"""

        from_attributes = True


class ShowUser(TunedModel):
    user_id: uuid.UUID
    name: str
    surname: str
    email: EmailStr


class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr

    @field_validator("name", "surname", mode="after")
    def validate_name_surname(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="Name and surname should contain letters"
            )
        return value
