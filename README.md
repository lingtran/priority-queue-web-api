# Priority Queue Web Api

## General information
Building a web API server priority queue to handle submitted jobs.

API here does not handle authentication and authorization.

* `Python 3.6.9`
* `Flask`
* `postgres`
* `Docker`
* `Docker Compose`
Install [Docker Compose](https://docs.docker.com/compose/install/)

## Setup

### `brew install pyenv`

This app uses for its Python version manager [pyenv](https://github.com/pyenv/pyenv#simple-python-version-management-pyenv). More installation instructions can be found [here](https://github.com/pyenv/pyenv#installation).

### `pyenv version`
```
> 3.6.9 
# Python version that should be returned
```

### `pyenv install 3.6.9`
...if the Python `3.6.9` is not already installed

### `pyenv local`
This will set the local Python version to what is specified in the `.python-version` file

### `python3 -m venv venv`
At project root directory, to create a `venv` folder

### `source venv/bin/activate`
To activate `venv`

### `deactivate`
To deactivate `venv`

### `pip3 install -r requirements.txt`
To install dependencies

### `CREATE DATABASE priority_queue_web_api_dev;`
`psql` command to create the database

### `flask db upgrade`
To run migrations after creating the database

### `flask run -h localhost -p 5000`
To spin up the application locally without database

### `docker-compose -f docker-compose.yml up`
From the project root to spin up the api and database with Docker