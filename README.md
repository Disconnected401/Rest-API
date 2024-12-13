Collecting workspace information

# REST API with Flask

This project is a simple REST API built using Flask. It allows you to manage a list of users with basic CRUD operations. The project includes both the API implementation and a set of unit tests to ensure its functionality.

## Files

- 

API.py

: Contains the implementation of the REST API.
- 

test_api.py

: Contains the unit tests for the REST API.

## API Endpoints

### Get All Users

- **URL**: 

users


- **Method**: `GET`
- **Response**: 
  - `200 OK`: Returns a list of all users.

### Get User by ID

- **URL**: `/users/<int:user_id>`
- **Method**: `GET`
- **Response**: 
  - `200 OK`: Returns the user with the specified ID.
  - `404 Not Found`: If the user does not exist.

### Create User

- **URL**: 

users


- **Method**: `POST`
- **Request Body**: JSON object with `name` and `lastname`.
- **Response**: 
  - `201 Created`: Returns the created user.
  - `400 Bad Request`: If the request body is missing `name` or `lastname`.

### Update User (Partial)

- **URL**: `/users/<int:user_id>`
- **Method**: `PATCH`
- **Request Body**: JSON object with `name` or `lastname`.
- **Response**: 
  - `204 No Content`: If the user is successfully updated.
  - `400 Bad Request`: If the user does not exist or the request body is invalid.

### Update User (Full)

- **URL**: `/users/<int:user_id>`
- **Method**: `PUT`
- **Request Body**: JSON object with `name` and `lastname`.
- **Response**: 
  - `204 No Content`: If the user is successfully updated or created.
  - `400 Bad Request`: If the request body is missing `name` or `lastname`.

### Delete User

- **URL**: `/users/<int:user_id>`
- **Method**: `DELETE`
- **Response**: 
  - `204 No Content`: If the user is successfully deleted.
  - `400 Bad Request`: If the user does not exist.

## Running the API

To run the API, execute the following command:

```sh
python API.py
```

The API will be available at `http://127.0.0.1:5000`.

## Running the Tests

To run the tests, execute the following command:

```sh
pytest test_api.py
```

The tests will verify the functionality of the API endpoints.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
