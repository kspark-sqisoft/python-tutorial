"""
연습문제 02: Pydantic Book 모델 정의 및 유효성 검사.

TODO:
1. Book 모델을 정의하라 (title: str, pages: int = Field(ge=1)).
2. 정상 데이터로 Book 인스턴스를 생성하고 model_dump() 를 확인하라.
3. 잘못된 데이터(pages=0) 로 생성 시 ValidationError 가 발생하는지 assert 하라.
"""

from pydantic import BaseModel, Field, ValidationError


# TODO: Book 모델을 정의하라.
# class Book(BaseModel):
#     ...


if __name__ == "__main__":
    # TODO: 정상 케이스 — title="파이썬 완전정복", pages=350 으로 Book 생성
    book = None  # 이 줄을 수정하라
    assert book is not None, "Book 인스턴스를 생성하라"
    assert book.title == "파이썬 완전정복"
    assert book.pages == 350

    # TODO: 잘못된 케이스 — pages=0 은 ValidationError 를 발생시켜야 한다.
    error_raised = False
    try:
        Book(title="빈 책", pages=0)  # noqa: F821
    except ValidationError:
        error_raised = True

    assert error_raised, "pages=0 일 때 ValidationError 가 발생해야 합니다"

    print("OK")
