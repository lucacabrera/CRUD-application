# create_books_table.py

import os
import csv
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# PostgreSQL connection URI — adjust if needed
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://lucacabrera:abcd123@localhost:5432/ukdsc"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Define the Book model
class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    published_date = db.Column(db.Date)


# Function to seed books from CSV
def seed_books(csv_path="books.csv"):
    if Book.query.first():
        print("📚 Books already seeded.")
        return

    abs_path = os.path.join(os.path.dirname(__file__), csv_path)

    with open(abs_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                # Parse date if needed
                pub_date = (
                    datetime.strptime(row["published_date"], "%Y-%m-%d").date()
                    if row["published_date"]
                    else None
                )
                new_book = Book(
                    title=row["title"],
                    author=row["author"],
                    published_date=pub_date,
                )
                db.session.add(new_book)
            except Exception as e:
                print(f"❌ Error adding book: {row} — {e}")
        db.session.commit()
        print("✅ Books seeded.")


# Run setup
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed_books()
        print("✅ 'books' table created and ready.")
