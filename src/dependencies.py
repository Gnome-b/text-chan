from typing import Annotated

from fastapi import Depends, HTTPException, Path

from crud.crud_post import get_post
from database import DbDependency
from models.post import PostModel
from schemas.secret_code import SecretCodeCheck
from security import verify_secret_code


async def verify_post_owner(
    db: DbDependency,
    secret_code: SecretCodeCheck,
    post_id: int = Path(ge=0),
) -> PostModel:
    post = await get_post(post_id=post_id, db=db)
    if post is None:
        raise HTTPException(status_code=404, detail="Пост не знайдено")
    if not await verify_secret_code(secret_code, post.secret_code_hash):
        raise HTTPException(status_code=403, detail="Невірний секретний код")
    return post


VerifiedPost = Annotated[PostModel, Depends(verify_post_owner)]
