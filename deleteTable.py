# delete_books_table.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Same PostgreSQL URI as before
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://lucacabrera:abcd123@localhost:5432/ukdsc"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Define the same model
class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    published_year = db.Column(db.Integer)


# Drop the table
with app.app_context():
    Book.__table__.drop(db.engine)
    print("🗑️ 'books' table deleted from PostgreSQL.")
