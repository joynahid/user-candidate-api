# Elevatus UserCandidateAPI Documentation

## Overview
The Elevatus UserCandidateAPI is a FastAPI based service designed for managing candidate user data. The API supports operations such as creating, updating, viewing, and deleting candidate profiles, as well as user management functionalities. Authentication is required for most endpoints.

Theere is a Swagger generated interactive docs:


### Version
- **API Version**: 0.1.0

## Authentication
Most API endpoints require authentication. Authentication is performed using an API key, which should be included in a cookie with the name `access_token`.

## Error Handling
Errors are returned as HTTP responses with a 422 status code, including a description of the validation error in the body.

## Endpoints

### Candidate Management

#### 1. Create Candidate
- **Endpoint**: `POST /candidate`
- **Description**: Create a new candidate entry in the candidates collection.
- **Request Body**: Required, `CandidateModel`
- **Response**: `CandidateModel` on success, `HTTPValidationError` on error.

#### 2. Update Candidate
- **Endpoint**: `PUT /candidate/{id}`
- **Description**: Update an existing candidate entry.
- **Parameters**: `id` (path, required)
- **Request Body**: Required, `UpdateCandidateModel`
- **Response**: `CandidateModel` on success, `HTTPValidationError` on error.

#### 3. View Candidate
- **Endpoint**: `GET /candidate/{id}`
- **Description**: Return a specific candidate's details.
- **Parameters**: `id` (path, required)
- **Response**: `CandidateModel` on success, `HTTPValidationError` on error.

#### 4. Delete Candidate
- **Endpoint**: `DELETE /candidate/{id}`
- **Description**: Delete a candidate entry from the collection.
- **Parameters**: `id` (path, required)
- **Response**: Success message on deletion, `HTTPValidationError` on error.

#### 5. Get All Candidates
- **Endpoint**: `GET /all-candidates`
- **Description**: List all candidates in the collection.
- **Parameters**: `search` (query, optional)
- **Response**: `CandidateListModel` on success, `HTTPValidationError` on error.

### Report Generation

#### 6. Generate CSV Report
- **Endpoint**: `GET /generate-report`
- **Description**: Generate a CSV report of all candidates.
- **Response**: CSV file content on success.

### User Management

#### 7. Create User
- **Endpoint**: `POST /user`
- **Description**: Create a new user in the users collection.
- **Request Body**: Required, `UserModel-Input`
- **Response**: `UserModel-Output` on success, `HTTPValidationError` on error.

#### 8. Get Current User
- **Endpoint**: `GET /user`
- **Description**: Retrieve the currently logged-in user's details.
- **Response**: `UserModel-Output` on success.

### Login

#### 9. Login
- **Endpoint**: `POST /login`
- **Description**: Authenticate a user.
- **Request Body**: Required, `UserLoginModel`
- **Response**: Success message on successful login, `HTTPValidationError` on error.

### Health Check

#### 10. Health Check
- **Endpoint**: `GET /health`
- **Description**: A simple health check API.
- **Response**: Success message on success.

## Schemas
The API uses various schemas to structure data for requests and responses. Key schemas include:

- `CandidateModel`: Represents a candidate profile.
- `UpdateCandidateModel`: Used for updating candidate data.
- `CandidateListModel`: A collection of `CandidateModel` objects.
- `UserModel-Input`: Represents a user profile for creation.
- `UserModel-Output`: Represents a user profile for output.
- `UserLoginModel`: Used for user login requests.
- `HTTPValidationError`: Structure for validation error messages.
- `ValidationError`: Details about specific validation errors.

For detailed schema definitions, including required fields and examples, refer to the `components/schemas` section of the API schema.

## Best Practices and Common Errors
- Ensure that all required fields in request bodies are included and correctly formatted.
- Handle HTTP 422 errors gracefully, parsing the `detail` field for specific validation issues.
- Always authenticate using the API key when accessing secured endpoints.
- When updating data, ensure that the provided ID matches the resource you intend to modify.

For further details and examples, please refer to the API's interactive swagger documentation.
