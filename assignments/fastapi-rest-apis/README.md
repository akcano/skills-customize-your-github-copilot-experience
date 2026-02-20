# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build modern, production-ready REST APIs using the FastAPI framework. You'll create a complete API with routing, request validation, error handling, and automatic documentation.

## 📝 Tasks

### 🛠️ Build a Basic API with Multiple Endpoints

#### Description
Create a FastAPI application that implements multiple endpoints to handle common HTTP operations. You will define routes that support GET and POST requests, develop request and response models using Pydantic, and implement proper HTTP status codes.

#### Requirements
Completed program should:

- Create at least 3 GET endpoints that return data in JSON format
- Implement at least 1 POST endpoint that accepts and validates request data
- Use Pydantic models to define request and response schemas
- Return appropriate HTTP status codes (200, 201, 400, 404)


### 🛠️ Add Data Validation and Error Handling

#### Description
Enhance your API with proper input validation and comprehensive error handling. Implement custom validation logic, handle edge cases, and provide meaningful error messages to API clients.

#### Requirements
Completed program should:

- Validate all incoming request data using Pydantic models
- Implement custom validation rules (e.g., age > 0, email format)
- Handle and return appropriate error responses with descriptive messages
- Use HTTP status codes 400 and 422 for validation errors


### 🛠️ Document and Test Your API

#### Description
Leverage FastAPI's automatic documentation generation and create test cases for your endpoints. Explore the interactive API documentation and verify that your implementation meets the requirements.

#### Requirements
Completed program should:

- Include docstrings and field descriptions for automatic API documentation
- Access the interactive documentation (Swagger UI) at `/docs`
- Write test cases for at least 3 endpoints
- Verify successful and error responses work as expected

