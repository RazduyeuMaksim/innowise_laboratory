from pydantic import BaseModel, Field
from typing import Optional


class BookRequest(BaseModel):
    """
    Class for the request to create or update a book
    """
    title: str = Field(
        min_length=1,
        max_length=255,
        description="The title of the book.",
        examples=["Title"]
    )

    author: str = Field(
        min_length=1,
        max_length=255,
        description="The author of the book.",
        examples=["Author"]
    )

    year: Optional[int] = Field(
        description="Publication year.",
        examples=[0]
    )


class BookResponse(BaseModel):
    """
     Class for API response with book information
    """
    id: int = Field(
        description="Unique identifier of the book.",
        examples=[1]
    )

    title: str = Field(
        min_length=1,
        max_length=255,
        description="The title of the book.",
        examples=["Title"]
    )

    author: str = Field(
        min_length=1,
        max_length=255,
        description="The author of the book.",
        examples=["Author"]
    )

    year: Optional[int] = Field(
        description="Publication year.",
        examples=[0]
    )

    class Config:
        from_attributes = True
