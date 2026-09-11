from typing import Annotated

from fastapi import Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession

from crud.crud_post import get_post
from database import DbDependency
from models.post import PostModel
from schemas.post import PostUpdateRequest, SecretCodeCheck
from security import verify_secret_code


async def verify_post_owner_for_upbate(
    db: DbDependency,
    body: PostUpdateRequest,
    post_id: int = Path(ge=0),
) -> PostModel:
    return await _verify_post_owner(
        db=db, secret_code=body.secret_code, post_id=post_id
    )


async def verify_post_owner_for_delete(
    db: DbDependency,
    body: SecretCodeCheck,
    post_id: int = Path(ge=0),
) -> PostModel:
    return await _verify_post_owner(
        db=db, secret_code=body.secret_code, post_id=post_id
    )


async def _verify_post_owner(
    db: AsyncSession,
    secret_code: str,
    post_id: int,
) -> PostModel:
    post = await get_post(post_id=post_id, db=db)
    if post is None:
        raise HTTPException(status_code=404, detail="Пост не знайдено")
    if not await verify_secret_code(secret_code, post.secret_code_hash):
        raise HTTPException(status_code=403, detail="Невірний секретний код")
    return post


VerifiedPost = Annotated[PostModel, Depends(verify_post_owner_for_upbate)]
VerifiedPost = Annotated[PostModel, Depends(verify_post_owner_for_delete)]
