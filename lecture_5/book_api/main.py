from typing import Annotated, Optional, List
from fastapi import FastAPI, Depends, HTTPException, Path
from database import engine, get_db
from sqlalchemy.orm import Session
from models import Book, Base
from starlette import status
from schemas import BookRequest, BookResponse

"""
FastAPI application instance
"""
app = FastAPI()

"""
Create all database tables at startup
"""
Base.metadata.create_all(bind=engine)

"""
Dependency for SQLAlchemy session
"""
db_dependency = Annotated[Session, Depends(get_db)]

"""
Add a new book to the database
"""
@app.post("/books/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
async def add_new_book(db: db_dependency, book_request: BookRequest):
    new_book = Book(**book_request.model_dump())

    try:
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    return new_book


"""
Get a list of all books
"""
@app.get("/books/", response_model=List[BookResponse], status_code=status.HTTP_200_OK)
async def get_all_books(db: db_dependency):
    return db.query(Book).all()


"""
Delete a book by its ID
"""
@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book_by_id(db: db_dependency, book_id: int = Path(gt=0)):
    book_model = db.query(Book).filter(Book.id == book_id).first()

    if book_model is None:
        raise HTTPException(status_code=404, detail="Book not found")

    try:
        db.delete(book_model)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    return


"""
Update book information by ID
"""
@app.put(
    "/books/{book_id}", 
    response_model=BookResponse, 
    status_code=status.HTTP_200_OK
)
async def update_book_by_id(
    db: db_dependency, 
    book_request: BookRequest, 
    book_id: int = Path(gt=0)
):
    book_model = db.query(Book).filter(Book.id == book_id).first()

    if book_model is None:
        raise HTTPException(status_code=404, detail="Book not found")

    book_model.title = book_request.title
    book_model.author = book_request.author
    book_model.year = book_request.year

    try:
        db.add(book_model)
        db.commit()
        db.refresh(book_model)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    return book_model


"""
Search books by title, author or year
"""
@app.get(
    "/books/search/", 
    response_model=List[BookResponse], 
    status_code=status.HTTP_200_OK
)
async def search_books(
    db: db_dependency,
    book_title: Optional[str] = None,
    book_author: Optional[str] = None,
    book_year: Optional[int] = None,
):
    query = db.query(Book)

    if book_title is not None:
        query = query.filter(Book.title == book_title)

    if book_author is not None:
        query = query.filter(Book.author == book_author)

    if book_year is not None:
        query = query.filter(Book.year == book_year)

    books = query.all()

    if not books:
        raise HTTPException(status_code=404, detail="Books not found")

    return books
