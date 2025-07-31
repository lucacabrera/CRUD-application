import json
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

from flask import Flask, render_template

# falsk setup
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/socket.io/")
@app.route("/socket.io/<path:path>")
def socket_io_stub(path=None):
    return "", 204


class Books(db.Model):
    __tablename__ = "books"

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


# CRUD:
# add a new book
@app.route("/books", methods=["POST"])
def createBook():
    bookData = request.get_json()
    new_book = Books(
        title=bookData["title"],
        author=bookData["author"],
        published_date=bookData["published_date"],
    )
    db.session.add(new_book)
    db.session.commit()
    return ({"message": "book created"}), 201


# get all books
@app.route("/books", methods=["GET"])
def getBooks():
    book = Books.query.all()
    books_list = [
        {
            "id": b.id,
            "title": b.title,
            "author": b.author,
            "published_date": b.published_date.strftime("%Y-%m-%d"),
        }
        for b in book
    ]
    return ({"message": "books retrieved", "books": books_list}), 200


# retrieve one book
@app.route("/books/<int:id>", methods=["GET"])
def getBook(id):
    book = Books.query.get_or_404(id)
    book_data = {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "published_date": book.published_date.strftime("%Y-%m-%d"),
    }
    return ({"message": "book retrieved", "book": book_data}), 200


# update a book
@app.route("/books/<int:id>", methods=["PUT"])
def updateBook(id):
    bookData = request.get_json()
    book = Books.query.get_or_404(id)
    book.title = bookData["title"]
    book.author = bookData["author"]
    book.published_date = bookData["published_date"]
    db.session.commit()
    return ({"message": "book updated"}), 200


# delete a book
@app.route("/books/<int:id>", methods=["DELETE"])
def deleteBook(id):
    book = Books.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return ({"message": "book deleted"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
