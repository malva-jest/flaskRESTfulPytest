# Flask RESTful CRUD Application

I have created a Flask RESTful CRUD application that provides basic functionality for a books API. Users can add, delete, update, and retrieve books using this app. The app also includes Pytest for testing the functionality of the app.

## Purpose of the Project

Overall, this project served as a learning experience for me. I used this project to learn about building APIs that are thoughtfully-designed and follow RESTful principles using Flask RESTful. Given my previous experience with Flask, I wanted to explore how Flask RESTful can simplify API development, including features such as request parsing and error handling. Additionally, I was also keen on integrating Test-Driven Development (TDD) to ensure that my code was of high quality and that my API worked as expected. Through TDD, automated tests helped me to identify and fix issues, potentially saving time and cost in a real-world development process. 

## Limitations of Flask RESTful

It is important to note that Flask-RESTful has not seen any new versions released on PyPI in the past 12 months. This could suggest that the project is discontinued or receiving low attention from its maintainers. While the Flask RESTful extension has many useful features, this lack of maintenance may lead to potential compatibility issues or security vulnerabilities.

To validate my thinking during development, I attempted a direct implementation of the tutorial on a to-do list in the Flask RESTful documentation but encountered issues with curl requests and continued to receive 403 errors for put and post methods despite a lot of trial and error. I welcome anyone with more experience with the framework to review the project and provide feedback.

While Flask-RESTful can be a useful tool in some cases, in my experience, it may not always be the best choice depending on the complexity of the project and the ability of the developer involved. 

## Getting Started

To get started with the Flask RESTful CRUD application, you'll need to have Python 3 installed on your machine. You can install the required dependencies by running the following command:

`pip install -r requirements.txt`

To run the app, navigate to the project directory and run the following command:

`python app.py`

The app should now be running on http://localhost:5000.

## Usage

The following API endpoints are available:

- `GET /books` - retrieve a list of all books
- `POST /books` - add a new book to the list
- `GET /books/<int:id>` - retrieve a book by ID
- `PUT /books/<int:id>` - update an existing book
- `DELETE /books/<int:id>` - delete a book by ID

To use these endpoints, you can use your preferred API client such as Postman, curl, or any other HTTP client.

## Testing

To run the included Pytest tests, run the following command:

`pytest test_app.py`

## Credits

This project was created by Matthew Alves.

## License

This project is licensed under the MIT license.