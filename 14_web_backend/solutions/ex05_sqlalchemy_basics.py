"""정답 05: SQLAlchemy in-memory DB 에 데이터 삽입·조회."""

from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id   = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)


if __name__ == "__main__":
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        session.add_all([
            User(name="홍길동"),
            User(name="이순신"),
        ])
        session.commit()

    with Session(engine) as session:
        users = session.execute(select(User)).scalars().all()

    assert len(users) == 2, f"사용자가 2명이어야 합니다. 실제: {len(users)}"

    print("OK")
