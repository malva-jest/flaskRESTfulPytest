
from flask import Flask, request, render_template
from flask_restful import reqparse, Resource, Api

app = Flask(__name__)

api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')

books = {
        1: {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year_published': 1925},
        2: {'title': 'Moby-Dick', 'author': 'Herman Melville', 'year_published': 1851},
        3: {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'year_published': 1951}
        }

def get_book(book_id):
    for key in books.keys():
        # key = books.get(keys)
        if key == book_id:
            return books[key]
    return None

parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('author')
parser.add_argument('year_published')

class Book(Resource):
    def get(self, book_id):
        book = get_book(book_id)
        if not book:
            abort(404, message="Book {} doesn't exist".format(book_id))
        return book

    def delete(self, book_id):
        book = get_book(book_id)
        if not book:
            abort(404, message="Book {} doesn't exist".format(book_id))
        books.pop(book_id)
        # No content status code
        return '', 204
    
    def put(self, book_id):
        args = parser.parse_args()
        if book_id in books:
            books[book_id]['title'] = args['title']
            books[book_id]['author'] = args['author']
            books[book_id]['year_published'] = args['year_published']
            return books[book_id], 200
        return "Book with ID {} not found".format(book_id), 404


class BookList(Resource):
    def get(self):
        return books

    def post(self, book_id):
        if get_book(book_id):
            abort(409, message="Book {} already exists".format(book_id))
        data = request.get_json()
        book = {
            'title': data['title'],
            'author': data['author'],
            'year_published': data['year_published']
        }
        books[book_id] = book
        return book, 201


api.add_resource(Book, '/books/<int:book_id>')
api.add_resource(BookList, '/books')

if __name__ == '__main__':
    app.run(debug=True)

