from pydantic import BaseModel, Field


class SecretCodeCheck(BaseModel):
    secret_code: str = Field(min_length=4, max_length=100)
