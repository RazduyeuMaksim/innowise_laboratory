from pydantic import BaseModel, Field
from typing import Optional

"""
Class for the request to create or update a book
"""
class BookRequest(BaseModel):
    title: str = Field(
        min_length=1,
        max_length=255,
        description="The title of the book.",
        example="Title"
    )
    author: str = Field(
        min_length=1,
        max_length=255,
        description="The author of the book.",
        example="Author"
    )
    year: Optional[int] = Field(
        description="Publication year.",
        example=0
    )


"""
 Class for API response with book information
"""
class BookResponse(BaseModel):
    id: int = Field(
        description="Unique identifier of the book.",
        example=1
    )
    title: str = Field(
        min_length=1,
        max_length=255,
        description="The title of the book.",
        example="Title"
    )
    author: str = Field(
        min_length=1,
        max_length=255,
        description="The author of the book.",
        example="Author"
    )
    year: Optional[int] = Field(
        description="Publication year.",
        example=0
    )

    class Config:
        from_attributes = True
