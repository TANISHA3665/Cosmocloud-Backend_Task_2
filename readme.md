# User Management using FastAPI and MongoDB

This is a FastAPI-based API for user and organization management using MongoDB.

## Setup
- Clone this repository
- Install the required packages by running pip install -r requirements.txt
- Start the API server by running uvicorn main:app --reload
- The API will be available at http://localhost:8000.

## Documentation
- The API documentation is available at http://localhost:8000/docs.

## Endpoints

### /users:
- GET /users: fetches all users or users filtered by name with pagination.
- GET /users/{user_id}: fetches a single user by ID.
- POST /users: creates a new user with a name and email.

### /orgs:
- GET /orgs: fetches all organizations or organizations filtered by name with pagination.
- GET /orgs/{org_name}: fetches a single organization by name.
- POST /orgs: creates a new organization with a unique name.

### /perms:
- PUT /perms/{user_id}/{org_name}: updates the permissions of a user on an organization.
- DELETE /perms/{user_id}/{org_name}: deletes the permissions of a user on an organization.

## Collections
- users
- orgs
- permissions

## Author
[Tanisha Jaiswal](https://github.com/TANISHA3665)

## Dependencies Used
- [FastAPI](https://fastapi.tiangolo.com/)
- [MongoDB](https://www.mongodb.com/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Uvicorn](https://www.uvicorn.org/)

[1]: https://fastapi.tiangolo.com/
[2]: https://www.mongodb.com/
[3]: https://pydantic-docs.helpmanual.io/
[4]: https://www.uvicorn.org/