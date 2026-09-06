from datetime import datetime, timezone

from sqlalchemy import DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class PostModel(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    author_name: Mapped[str | None] = mapped_column(String(50))
    subject: Mapped[str | None] = mapped_column(String(100))
    text: Mapped[str] = mapped_column(Text)
    secret_code_hash: Mapped[str] = mapped_column(String(60))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), index=True
    )
