import json
import pytest
import requests
from flask_restful import Api, Resource
from app import Book, get_book
from app import books

def test_get_book_success():
    book_id = 1
    expected_book = {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year_published': 1925}
    # expected_book = {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year_published': 1925}
    result = get_book(book_id)
    assert result == expected_book

def test_get_book_failure():
    book_id = 4
    expected_result = None
    result = get_book(book_id)
    assert result == expected_result

def test_delete_book():
    # Create a book to delete
    book = {'title': 'Test Book', 'author': 'Test Author', 'year_published': 2020}
    book_id = max(books.keys()) + 1
    # book_id = str(book['title'])
    books[book_id] = book
    
    # Call the delete method
    resource = Book()
    result = resource.delete(book_id)
    
    # Assert the book was deleted and the correct status code was returned
    assert result == ('', 204)
    assert book_id not in books


def test_post_book():
    url = "http://localhost:5000/books"
    # headers = {'Content-Type': 'application/json'}
    new_book = {
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'year_published': 1960
    }
    response = requests.post(url, json=new_book)

    # Used print statements to see if the method is being called correctly
    print("Request URL:", response.url)
    print("Request Headers:", response.request.headers)
    print("Request Body:", response.request.body)
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.content)

    assert response.status_code == 201
    assert response.json() == new_book

def test_put_book():
    url = "http://localhost:5000/books/1"
    updated_book = {
        'title': 'The Great Gatsby (updated)',
        'author': 'F. Scott Fitzgerald (updated)',
        'year_published': 1926
    }
    response = requests.put(url, json=updated_book)

    print("Request URL:", response.url)
    print("Request Headers:", response.request.headers)
    print("Request Body:", response.request.body)
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.content)

    assert response.status_code == 200
    assert response.json() == {'title': 'The Great Gatsby (updated)', 'author': 'F. Scott Fitzgerald (updated)', 'year_published': 1926}

