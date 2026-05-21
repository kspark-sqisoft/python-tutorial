"""정답 02: Pydantic Book 모델 정의 및 유효성 검사."""

from pydantic import BaseModel, Field, ValidationError


class Book(BaseModel):
    title: str
    pages: int = Field(ge=1)


if __name__ == "__main__":
    book = Book(title="파이썬 완전정복", pages=350)
    assert book.title == "파이썬 완전정복"
    assert book.pages == 350

    error_raised = False
    try:
        Book(title="빈 책", pages=0)
    except ValidationError:
        error_raised = True

    assert error_raised, "pages=0 일 때 ValidationError 가 발생해야 합니다"

    print("OK")
