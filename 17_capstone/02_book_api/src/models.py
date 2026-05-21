"""ORM 모델: Book."""

from sqlalchemy.orm import Mapped, mapped_column

from .db import Base


class Book(Base):
    """SQLAlchemy ORM model for a book record."""

    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    pages: Mapped[int]
