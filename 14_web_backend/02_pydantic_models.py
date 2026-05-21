"""
Pydantic v2 를 이용한 데이터 모델 검증·직렬화 학습.
BaseModel, Field, ValidationError 를 사용해
타입 안전한 데이터 구조를 정의하고 활용한다.
"""

from pydantic import BaseModel, Field, ValidationError

# ──── 1. 기본 모델 정의 ────

class User(BaseModel):
    """사용자 데이터 모델 — 필드 타입과 제약을 선언한다."""
    name: str
    age: int = Field(ge=0, description="나이는 0 이상이어야 한다")
    email: str = ""           # 기본값 있는 선택 필드


class Address(BaseModel):
    """주소 모델 — 중첩 모델 예시."""
    city: str
    zipcode: str = Field(pattern=r"^\d{5}$", description="5자리 숫자 우편번호")


class UserWithAddress(BaseModel):
    """중첩 모델 — User 에 Address 를 포함한다."""
    user: User
    address: Address


# ──── 2. 직렬화 ────

def serialize_demo(user: User) -> None:
    """dict / JSON 직렬화를 보여준다."""
    print(f"  model_dump()        : {user.model_dump()}")
    print(f"  model_dump_json()   :\n{user.model_dump_json(indent=2)}")


# ──── 3. 역직렬화 ────

def deserialize_demo() -> User:
    """dict / JSON 문자열에서 모델을 복원한다."""
    # dict 로부터
    u1 = User.model_validate({"name": "Kee", "age": 30, "email": "kee@example.com"})

    # JSON 문자열로부터
    json_str = '{"name": "순이", "age": 25}'
    u2 = User.model_validate_json(json_str)

    print(f"  dict 복원  : {u1}")
    print(f"  JSON 복원  : {u2}")
    return u1


# ──── 4. 유효성 검사 실패 ────

def validation_error_demo() -> None:
    """잘못된 데이터는 ValidationError 를 발생시킨다."""
    bad_cases = [
        {"name": "음수나이", "age": -5},          # age < 0
        {"name": 123, "age": "not-a-number"},      # 잘못된 타입
        {},                                         # 필수 필드 누락
    ]
    for case in bad_cases:
        try:
            User(**case)
        except ValidationError as e:
            # error_count() 로 오류 개수를 확인할 수 있다
            print(f"  입력 {case} → 오류 {e.error_count()}개")


if __name__ == "__main__":
    print("=== 02_pydantic_models.py 데모 ===\n")

    # 정상 케이스
    print("1) 정상 데이터 생성 및 직렬화")
    user = User(name="홍길동", age=28, email="hong@example.com")
    serialize_demo(user)

    print("\n2) 역직렬화")
    deserialize_demo()

    print("\n3) 유효성 검사 실패 케이스")
    validation_error_demo()

    print("\n4) 중첩 모델")
    ua = UserWithAddress(
        user=User(name="이순신", age=45),
        address=Address(city="서울", zipcode="04524"),
    )
    print(f"  중첩 dump : {ua.model_dump()}")

    print("\n완료!")
