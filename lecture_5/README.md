# lecture_5

## 🚀 Simple Book Collection API

### Description
A simple RESTful API built with FastAPI and SQLAlchemy for managing a collection of books.

The API allows you to:

- Add new books to the database  
- Retrieve a list of all books  
- Update book information by ID  
- Delete books by ID  
- Search books by title, author, or publication year  

The application uses SQLite as a database and SQLAlchemy ORM for data access.

---

###  API output
The API provides JSON responses that include:

- Full book information (id, title, author, year)  
- Lists of books based on search criteria  
- Proper HTTP status codes for success and errors  

---

### Notes
- Built with FastAPI for high-performance REST API development  
- Uses SQLAlchemy ORM with SQLite  
- Pydantic schemas validate request and response data  
- Handles invalid input and missing resources gracefully