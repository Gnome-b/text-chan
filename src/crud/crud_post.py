from sqlalchemy import select

from database import DbDependency
from models.post import PostModel
from schemas.post import PostCreate
from security import hash_secret_code


async def create_post(post_data: PostCreate, db: DbDependency) -> PostModel:
    hashed = await hash_secret_code(post_data.secret_code)
    new_post = PostModel(
        author_name=post_data.author_name or "Anonym",
        subject=post_data.subject,
        text=post_data.text,
        secret_code_hash=hashed,
    )
    db.add(new_post)
    await db.commit()
    await db.refresh(new_post)
    return new_post


async def get_post(post_id: int, db: DbDependency) -> PostModel | None:
    result = await db.execute(select(PostModel).where(PostModel.id == post_id))
    return result.scalar_one_or_none()
