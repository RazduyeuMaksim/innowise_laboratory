from pydantic import BaseModel, Field
from typing import Optional

"""
Class for the request to create or update a book
"""
class BookRequest(BaseModel):
    title: str = Field(
        min_length=1,
        max_length=255,
        json_schema_extra={
            "title": "Book Title",
            "description": "The title of the book.",
            "example": "Title",
        },
    )
    author: str = Field(
        min_length=1,
        max_length=255,
        json_schema_extra={
            "title": "Book Author",
            "description": "The author of the book.",
            "example": "Author",
        },
    )
    year: Optional[int] = Field(
        json_schema_extra={
            "title": "Publication Year",
            "description": "Publication year.",
            "example": 0,
        },
    )


"""
 Class for API response with book information
"""
class BookResponse(BaseModel):
    id: int = Field(
        description="Unique identifier of the book.",
        json_schema_extra={"example": 1},
    )
    title: str = Field(
        min_length=1,
        max_length=255,
        description="The title of the book.",
        json_schema_extra={"example": "Title"},
    )
    author: str = Field(
        min_length=1,
        max_length=255,
        description="The author of the book.",
        json_schema_extra={"example": "Author"},
    )
    year: Optional[int] = Field(
        description="Publication year.",
        json_schema_extra={"example": 0},
    )

    model_config = {"from_attributes": True}
