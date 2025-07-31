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

* [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
* [![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
* [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
* [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)


## Getting Started

To set this project up locally, and get a copy up and running, follow these simple steps. This is for macOS only.

### Prerequsites

These are the tools you need to run the software and how to install them on macOS using Homebrew.

* **Homebrew**

If you don’t have Homebrew installed, install it first by running:
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

* **Docker**
 
Install docker by running:
```
brew install docker
```

and then download the app from [Docker's website](https://www.docker.com/).

* **Postman (Optional)**

For running commands with a more user-friendly UI you might want to use Postman. Install postman by running:
```
brew install --cask postman
``` 

### Installation

**1. Clone the repo**

Run this command in your terminal:
```bash
git clone https://github.com/lucacabrera/ukdsc-project.git
cd ukdsc-project
```
**2. Build and start the containers**

Make sure the docker app is open, and logged in. Then, run the following command to start the containers:
```
docker-compose up --build
```

**3. Initialise the database**

After the containers are running we can migrate the database. In a new terminal window run this (don't close the other terminal):
```
docker-compose exec web flask db upgrade
```

### Usage

You can use the app using cURL commands, or if you installed it, postman. 

#### **cURL Commands:**

All these commands should be run in a terminal window.

**1. POST**

Put a new book on the database.

```
curl -X POST http://localhost:5000/books \
-H "Content-Type: application/json" \
-d '{"title": "[title]", "author": "[author]", "published_date": "[yyyy-mm-dd]"}'
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
curl -X PUT http://localhost:5000/books/1 \
-H "Content-Type: application/json" \
-d '{"title": "[title]", "author": "[author]", "published_date": "[yyyy-mm-dd]"}'
```

**4. DELETE**

Delete a book off of the database
```
curl -X DELETE http://localhost:5000/books/[id]
```


#### Postman
Start by selecting new in your workspace, and choose the HTTP option.

**1. POST**

* Method: `POST`

* URL: `http://localhost:5000/books`

* Body → Raw → JSON:
```
{
  "title": "[title]",
  "author": "[author]",
  "published_date": "[yyyy-mm-dd]"
}
```

**2. GET**

To get all books from the database
* Method: `GET`

* URL: `http://localhost:5000/books`

To get a specific book from the database
* Method: `GET`

* URL: `http://localhost:5000/books/[id]`

**3. PUT**

To update a book on the database
* Method: `PUT`

* URL: `http://localhost:5000/books/[id]`

* Body → Raw → JSON:
```
{
  "title": "[title]",
  "author": "[author]",
  "published_date": "[yyyy-mm-dd]"
}
```

**4. DELETE**

To delete a book from the database
* Method: `DELETE`

* URL: `http://localhost:5000/books/[id]`
