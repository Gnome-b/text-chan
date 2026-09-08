from sqlalchemy import desc, select

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


async def get_posts(page: int, limit: int, db: DbDependency) -> list[PostModel]:
    offset = (page - 1) * limit
    result = await db.execute(
        select(PostModel)
        .order_by(desc(PostModel.created_at))
        .offset(offset)
        .limit(limit)
    )
    return result.scalar().all()
