import json
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#flask setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/bookstore"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Books(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text())
    author = db.Column(db.Text())
    published_date = db.Column(db.Date())

    def __init__(self, title, author, published_date):
        self.title = title
        self.author = author
        self.published_date = published_date

    def __repr__(self):
        return f"<Book {self.title}>"
    


Book = [
        { 'id': 1, 'title': '1984', 'author': 'George Orwell', 'published_date': '1949' },
        {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'published_date': '1960'},
        {'id': 3, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'published_date': '1925'}
        ]

#CRUD:
#create a new book
@app.route('/books', methods=['POST'])
def createBook():
    new_book = request.get_json()
    Book.append(new_book)
    return jsonify(Book)

#read info about a book
@app.route('/books', methods=['GET'])
def getBooks():
    return jsonify(Book)

#update a book
@app.route('/books/<int:id>', methods=['PUT'])
def updateBook(id):
    book = getBooks(id)
    Book[id] = request.get_json()
    return jsonify(Book)

#delete a book
@app.route('/books/<int:id>', methods=['DELETE'])
def deleteBook(id):
    Book.pop(id)
    return jsonify(Book)

if __name__ == "__main__":
    app.run(debug=True)