from datetime import datetime

from pydantic import BaseModel, Field

class PostCreate(BaseModel):
    author_name: str | None = Field(default=None, max_length=50)
    subject: str | None = Field(default=None, max_length=100)
    text: str = Field(min_length=1, max_length=5000)
    secret_code: str = Field(min_length=4, max_length=100)

class PostResponse(BaseModel):
    id: int
    author_name: str
    subject: str | None
    text: str
    created_at: datetime
