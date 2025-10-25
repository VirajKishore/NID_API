# **Logs**

I am going to log my progress

#### Env Setup

Struggled with getting virtualenvwrapper installed as I had to install it using homebrew and there was an error ("missing double quote") in the .zshrc file.

Installed virtualenvwrapper

FastAPI now runs on venvwrapper called nid_api. use wokon nid_api

Installed fast API

#### SQLAlchemy

Installed sqlalchemy
**SQLAlchemy** is a **Python library** that lets you work with databases in a cleaner, more Pythonic way — _without_ writing raw SQL all the time.

Think of it like this: Object Relational Mapper

> Instead of writing `"SELECT * FROM users WHERE id = 5;"`, you just say
>
> `session.query(User).filter(User.id == 5).first()`

Created file structure
main.py, models folder [models, database, init], schemas.py and requirements.txt

Git Issues:

- Had to log out of old git hub account
- Had to use the line below to switch to ssh from password based auth
  - git remote set-url origin git@github.com:VirajKishore/NID_API.git

Created model note in model.py with columns id, title, body, last_updated

Last Updated Status:

    Need to figure out to how implement migrations with versions.

#### Installed Alembic for migrations

Note: This migration part was not from the guide. The guide has proposed a hack in the __init__.py to generate db with the tables if it does not exist but it is not the standard way to manage migrations in big scale products. Hence I asked chatGPT to guide me to follow the standard way. This way we have versions, control with scripts.

```python
pip install alembic

#initialzie alembic
alembic init alembic
```

The above has created a new folder alembic with /versions, env.py, readme and script.py.mako, and alembic.ini in the root folder.

* Change sqlalchemy.url to the db path in alembic.ini
* Change metadata in alembic/.env
  ```python
  from model import models
  target_metadata = models.Base.metadata
  ```
* Now we need to create our first migration based on out Note model.
* ```bash
  alembic revision --autogenerate -m "Initial migration"
  ```
* It did not work initially because I mispelt sqlite as sqllite in alembic.in sqlalchemy.url path.
* After correcting the aboce, nid.db is created in versions/ a file is created migration script.
* To create table in the genrated db by running the migration script,
* ```bash
  alembic upgrade head
  ```
* Now the table is created in the nid.db

#### API Setup (and hooking the created layer to the API)

* We initialize FastAPI using FastAPI() constructor that helps taking care of routing, json validation using pydantic and API docs using Swagger and middleware.
* Using @app,get("/notes"}) to add a get request which returns all notes. We should declare a DBSession and use it to query the DB for all notes.
*
