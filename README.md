# Django-Auth-API
This is a Django-based authentication API that provides endpoints for user registration and login. It’s designed to be simple, secure, and efficient, making it easy to manage user accounts in your applications.
# Django Auth API

This is a Django-based authentication API that provides endpoints for user registration and login. It's designed to be simple, secure, and efficient, making it easy to manage user accounts in your applications.

## Features

- **User Registration**: Allows new users to create an account. The registration endpoint accepts email, password, location, first name, and last name as required fields. It ensures that the email provided during registration is unique across all users.

- **User Login**: Allows existing users to authenticate using their email and password. Upon successful authentication, it returns a token that can be used for authenticated requests.

- **Token Authentication**: This API uses token-based authentication, which is a common way to handle user authentication in API views. The token is generated upon successful login and must be included in the HTTP header for authenticated requests.

- **Custom User Model**: Uses a custom user model that extends Django's built-in `AbstractUser` model. The custom user model uses email as the username field for authentication.

- **Error Handling**: Provides clear error messages for validation errors. For example, if a user tries to register with an email that's already in use, the API will return a custom error message.

## Usage

To register a new user, send a `POST` request to the `/register/` endpoint with the required fields. To authenticate an existing user, send a `POST` request to the `/login/` endpoint with the user's email and password.

## Installation

This API is built with Django and Django Rest Framework. To install it, you'll need to have Python installed on your machine. You can then install the necessary packages using pip:

```bash
pip install django djangorestframework