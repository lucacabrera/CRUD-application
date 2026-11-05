<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>

## About the project

A Flask API for a bookstore database, which uses GET, POST, PUT and DELETE commands to use CRUD operations for books in the bookstore database.

### Built With

- [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
- [![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
- [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
- [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
- [![HTML](https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://www.html.com/)
- [![CSS](https://img.shields.io/badge/CSS-663399?style=for-the-badge&logo=css&logoColor=white)](https://www.html.com/)
- [![Javascript](https://img.shields.io/badge/Javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white)](https://www.html.com/)

## Getting Started

To set this project up locally, and get a copy up and running, follow these simple steps. This is for macOS only.

### Prerequsites

These are the tools you need to run the software and how to install them on macOS using Homebrew.

- **Homebrew**

If you don’t have Homebrew installed, install it first by running:

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- **Docker**

Install docker by running:

```
brew install docker
```

and then download the app from [Docker's website](https://www.docker.com/).

- **Postman (Optional)**

For running commands with a more user-friendly UI you might want to use Postman. Install postman by running:

```
brew install --cask postman
```

### Installation

**1. Clone the repo**

Run this command in your terminal:

```bash
git clone https://github.com/lucacabrera/CRUD-application.git
cd CRUD-application
```

**2. Build and start the containers**

Run the following command to start the containers:

```
docker-compose up --build
```

**3. Initialise the database**

After the containers are running we can migrate the database:

```
docker-compose exec web flask db upgrade
```

### Usage

### Backend Usage (Terminal)

You can use the app using cURL commands, or if you installed it, postman.

#### **cURL Commands:**

All these commands should be run in a terminal window.

**1. POST**

Put a new book on the database.

```
curl -X POST http://localhost:5000/books \
-H "Content-Type: application/json" \
-d '{"title": "title", "author": "author", "published_date": "yy-mm-dd"}'
```

**2. GET**

To get all books from the database

```
curl http://localhost:5000/books
```

To get a specific book from the database

```
curl http://localhost:5000/books/[id]
```

**3. PUT**

To update a book on the database

```
curl -X PUT http://localhost:5000/books \
-H "Content-Type: application/json" \
-d '{"title": "title", "author": "author", "published_date": "yy-mm-dd"}'
```

**4. DELETE**

Delete a book off of the database

```
curl -X DELETE http://localhost:5000/books/[id]
```

#### Postman

Start by selecting new in your workspace, and choose the HTTP option.

**1. POST**

- Method: `POST`

- URL: `http://localhost:5000/books`

- Body → Raw → JSON:

```
{
  "title": "[title]",
  "author": "[author]",
  "published_date": "[yyyy-mm-dd]"
}
```

**2. GET**

To get all books from the database

- Method: `GET`

- URL: `http://localhost:5000/books`

To get a specific book from the database

- Method: `GET`

- URL: `http://localhost:5000/books/[id]`

**3. PUT**

To update a book on the database

- Method: `PUT`

- URL: `http://localhost:5000/books/[id]`

- Body → Raw → JSON:

```
{
  "title": "[title]",
  "author": "[author]",
  "published_date": "[yyyy-mm-dd]"
}
```

**4. DELETE**

To delete a book from the database

- Method: `DELETE`

- URL: `http://localhost:5000/books/[id]`

### Frontend Usage

You can go to `http://13.60.254.2:5000/` and use the app with a GUI.

**1. Creating books:**

To update a book from the database, use the form menu on the main page of the site.

Enter a title in the title box, author in the author box and the publishing date in the calender. You can also optionally add an icon for the book for the table.

**2. Viewing books:**

Click on the view tab in the navbar to see all the books in the database. Newly updated/created books will be at the bottom of the page.

**3. Updating books**

On the view page, click on an icon to bring up the actions modal. Press update, and change the data that needs to changed on the new popup. Then press save changes, and close.

**4. Deleting books**

On the view page, click on an icon to bring up the actions modal. Press delete, and the entry will be deleted.
