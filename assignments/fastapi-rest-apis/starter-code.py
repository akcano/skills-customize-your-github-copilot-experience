"""
FastAPI REST API Starter Code
Building REST APIs with FastAPI

Instructions:
1. Install FastAPI and Uvicorn: pip install fastapi uvicorn
2. Complete the tasks in the assignment README
3. Run the application: uvicorn starter-code:app --reload
4. Visit http://localhost:8000/docs to see interactive documentation
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List


# Initialize FastAPI application
app = FastAPI(
    title="Student Management API",
    description="A simple API for managing student records",
    version="1.0.0"
)


# Define Pydantic models for request/response validation
class StudentBase(BaseModel):
    name: str = Field(..., min_length=1, description="Student's full name")
    email: str = Field(..., description="Student's email address")
    age: int = Field(..., gt=0, lt=120, description="Student's age")
    grade: Optional[str] = Field(None, description="Student's grade level")


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    id: int = Field(..., description="Student's unique ID")

    class Config:
        from_attributes = True


# Sample in-memory data storage (replace with database in production)
students_db = [
    {"id": 1, "name": "Alice Johnson", "email": "alice@example.com", "age": 16, "grade": "10th"},
    {"id": 2, "name": "Bob Smith", "email": "bob@example.com", "age": 17, "grade": "11th"},
]


# TODO: Implement GET endpoints
# 1. GET /students - Return all students
# 2. GET /students/{student_id} - Return a specific student by ID
# 3. GET /students/search - Search students by name (query parameter)

# Example endpoint structure:
# @app.get("/students", response_model=List[Student])
# async def get_all_students():
#     """Retrieve all students from the database."""
#     return students_db


# TODO: Implement POST endpoint
# 1. POST /students - Create a new student
# 2. Validate input using StudentCreate model
# 3. Assign a new ID (max current ID + 1)
# 4. Return created student with 201 status code

# Example endpoint structure:
# @app.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
# async def create_student(student: StudentCreate):
#     """Create a new student record."""
#     # Implementation here
#     pass


# TODO: Implement error handling
# - Return 404 when student not found
# - Return 400 for invalid input
# - Return 422 for validation errors (automatic with Pydantic)


# Root endpoint - Test that API is running
@app.get("/", tags=["Health"])
async def root():
    """Health check endpoint."""
    return {
        "message": "Student Management API is running!",
        "documentation": "Visit /docs for interactive API documentation"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
