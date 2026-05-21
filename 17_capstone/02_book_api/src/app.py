"""FastAPI 앱: Book CRUD API."""

from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from .db import Base, engine, get_session
from .models import Book
from .schemas import BookIn, BookOut


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """앱 시작 시 DB 테이블 생성."""
    Base.metadata.create_all(engine)
    yield


app = FastAPI(title="Book API", lifespan=lifespan)


@app.get("/books", response_model=list[BookOut])
def list_books(session: Session = Depends(get_session)) -> list[Book]:
    """모든 책 목록 반환."""
    return list(session.execute(select(Book)).scalars().all())


@app.post("/books", response_model=BookOut, status_code=201)
def create_book(body: BookIn, session: Session = Depends(get_session)) -> Book:
    """새 책 생성."""
    book = Book(title=body.title, pages=body.pages)
    session.add(book)
    session.commit()
    session.refresh(book)
    return book


@app.get("/books/{book_id}", response_model=BookOut)
def get_book(book_id: int, session: Session = Depends(get_session)) -> Book:
    """단일 책 조회 (없으면 404)."""
    book = session.get(Book, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int, session: Session = Depends(get_session)) -> None:
    """책 삭제 (없으면 404)."""
    book = session.get(Book, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    session.delete(book)
    session.commit()


if __name__ == "__main__":
    from fastapi.testclient import TestClient

    Base.metadata.create_all(engine)
    client = TestClient(app)

    # POST 시연
    resp = client.post("/books", json={"title": "파이썬 완전 정복", "pages": 420})
    print("POST /books →", resp.status_code, resp.json())

    # GET 시연
    resp = client.get("/books")
    print("GET  /books →", resp.status_code, resp.json())
