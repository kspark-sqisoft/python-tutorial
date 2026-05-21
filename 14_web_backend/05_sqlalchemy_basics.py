"""
SQLAlchemy 2.x ORM 기초 — in-memory SQLite 로 실습.
실제 파일 DB 없이 메모리 안에서 테이블 생성·삽입·조회를 경험한다.
declarative_base, Session, select 를 중심으로 학습한다.
"""

from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import declarative_base, Session

# ──── 1. 엔진 및 Base 설정 ────

# sqlite:///:memory: → 프로세스 종료 시 사라지는 인메모리 DB
engine = create_engine("sqlite:///:memory:", echo=False)

Base = declarative_base()   # 모든 ORM 모델의 부모 클래스


# ──── 2. 모델(테이블) 정의 ────

class User(Base):
    """users 테이블 — ORM 모델."""
    __tablename__ = "users"

    id   = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    age  = Column(Integer, nullable=True)

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name!r}, age={self.age})"


class Product(Base):
    """products 테이블 — 두 번째 모델 예시."""
    __tablename__ = "products"

    id    = Column(Integer, primary_key=True, autoincrement=True)
    name  = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Product(id={self.id}, name={self.name!r}, price={self.price})"


# ──── 3. 테이블 생성 ────

def init_db() -> None:
    """선언된 모든 모델로 테이블을 생성한다."""
    Base.metadata.create_all(engine)


# ──── 4. 데이터 삽입 ────

def insert_sample_data() -> None:
    """샘플 데이터 3행을 삽입한다."""
    users = [
        User(name="홍길동", age=30),
        User(name="이순신", age=45),
        User(name="유관순", age=17),
    ]
    products = [
        Product(name="사과", price=1500),
        Product(name="노트북", price=1_200_000),
    ]
    with Session(engine) as session:
        session.add_all(users)
        session.add_all(products)
        session.commit()   # 트랜잭션 커밋


# ──── 5. 데이터 조회 ────

def query_all_users() -> list[User]:
    """모든 사용자를 조회한다."""
    with Session(engine) as session:
        stmt = select(User)                         # SELECT * FROM users
        return session.execute(stmt).scalars().all()


def query_users_by_age(min_age: int) -> list[User]:
    """나이가 min_age 이상인 사용자를 조회한다."""
    with Session(engine) as session:
        stmt = select(User).where(User.age >= min_age).order_by(User.age)
        return session.execute(stmt).scalars().all()


def query_products() -> list[Product]:
    """모든 상품을 가격 내림차순으로 조회한다."""
    with Session(engine) as session:
        stmt = select(Product).order_by(Product.price.desc())
        return session.execute(stmt).scalars().all()


# ──── 6. 데이터 수정 / 삭제 ────

def update_user_age(user_id: int, new_age: int) -> None:
    """특정 사용자의 나이를 수정한다."""
    with Session(engine) as session:
        user = session.get(User, user_id)   # PK 로 단건 조회
        if user:
            user.age = new_age
            session.commit()


def delete_user(user_id: int) -> None:
    """특정 사용자를 삭제한다."""
    with Session(engine) as session:
        user = session.get(User, user_id)
        if user:
            session.delete(user)
            session.commit()


if __name__ == "__main__":
    print("=== 05_sqlalchemy_basics.py 데모 ===\n")

    # 초기화
    init_db()
    print("1) 테이블 생성 완료")
    print(f"   테이블: {list(Base.metadata.tables.keys())}")

    # 삽입
    insert_sample_data()
    print("\n2) 샘플 데이터 삽입 완료")

    # 전체 조회
    users = query_all_users()
    print(f"\n3) 전체 사용자 ({len(users)}명)")
    for u in users:
        print(f"   {u}")

    # 조건 조회
    adults = query_users_by_age(20)
    print(f"\n4) 나이 20 이상 사용자 ({len(adults)}명)")
    for u in adults:
        print(f"   {u}")

    # 상품 조회
    products = query_products()
    print(f"\n5) 상품 목록 (가격 내림차순, {len(products)}개)")
    for p in products:
        print(f"   {p}")

    # 수정
    update_user_age(1, 31)
    updated = query_all_users()
    print(f"\n6) id=1 나이 수정 후: {updated[0]}")

    # 삭제
    delete_user(3)
    after_delete = query_all_users()
    print(f"\n7) id=3 삭제 후 사용자 수: {len(after_delete)}명")

    print("\n완료! (모든 데이터는 인메모리 — 프로세스 종료 시 소멸)")
