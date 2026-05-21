"""
연습문제 05: SQLAlchemy in-memory DB 에 데이터 삽입·조회.

TODO:
1. User 모델(id, name)을 정의하라.
2. in-memory SQLite 엔진을 생성하고 테이블을 만들어라.
3. 사용자 2명을 삽입하고 커밋하라.
4. 전체 조회 결과 길이가 2 임을 assert 하라.
"""

from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import declarative_base, Session


Base = declarative_base()


# TODO: User 모델을 정의하라 (__tablename__ = "users", id, name 컬럼).
# class User(Base):
#     ...


if __name__ == "__main__":
    # TODO: in-memory 엔진을 생성하고 테이블을 만들어라.
    engine = None  # create_engine("sqlite:///:memory:") 으로 교체하라

    # TODO: engine 이 None 이 아닐 때만 테이블 생성
    # Base.metadata.create_all(engine)

    # TODO: Session 으로 User 2명을 삽입하고 커밋하라.
    # with Session(engine) as session:
    #     ...

    # TODO: 전체 사용자를 조회하라.
    users = []  # select(User) 결과로 교체하라

    assert len(users) == 2, f"사용자가 2명이어야 합니다. 실제: {len(users)}"

    print("OK")
