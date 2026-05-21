"""I/O 스키마."""

from pydantic import BaseModel, ConfigDict, Field


class BookIn(BaseModel):
    """입력 스키마: 책 생성/수정 요청."""

    title: str = Field(min_length=1)
    pages: int = Field(ge=1)


class BookOut(BookIn):
    """출력 스키마: 책 응답 (id 포함)."""

    id: int
    model_config = ConfigDict(from_attributes=True)
