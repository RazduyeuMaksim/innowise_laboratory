# lecture_4

## 🚀 Student Grade Manager

### Description
A simple Python program for initializing and managing a student grade database using SQLite.

The program allows you to:

- Create a relational database for students and grades  
- Enforce data integrity with foreign keys and constraints  
- Populate the database with sample data  
- Run predefined analytical SQL queries  

All database logic is executed from an external SQL file.

---

### Profile output
The database supports queries that provide:

- Average grade per student  
- Average grade per subject  
- Top 3 students by average grade  
- Students with grades below a given threshold  
- Students filtered by birth year  

---

### Notes
- Uses SQLite (`sqlite3`) from the Python standard library  
- Clean separation between Python logic and SQL logic  
- SQL script includes indexes for performance optimization  
- Foreign key constraints are enabled (`PRAGMA foreign_keys = ON`)  
