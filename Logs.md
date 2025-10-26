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

Note: This migration part was not from the guide. The guide has proposed a hack in the **init**.py to generate db with the tables if it does not exist but it is not the standard way to manage migrations in big scale products. Hence I asked chatGPT to guide me to follow the standard way. This way we have versions, control with scripts.

```python
pip install alembic

#initialzie alembic
alembic init alembic
```

The above has created a new folder alembic with /versions, env.py, readme and script.py.mako, and alembic.ini in the root folder.

- Change sqlalchemy.url to the db path in alembic.ini
- Change metadata in alembic/.env
  ```python
  from model import models
  target_metadata = models.Base.metadata
  ```
- Now we need to create our first migration based on out Note model.
- ```bash
  alembic revision --autogenerate -m "Initial migration"
  ```
- It did not work initially because I mispelt sqlite as sqllite in alembic.in sqlalchemy.url path.
- After correcting the aboce, nid.db is created in versions/ a file is created migration script.
- To create table in the genrated db by running the migration script,
- ```bash
  alembic upgrade head
  ```
- Now the table is created in the nid.db

#### API Setup (and hooking the created layer to the API)

- We initialize FastAPI using FastAPI() constructor that helps taking care of routing, json validation using pydantic and API docs using Swagger and middleware.
- Using @app,get("/notes"}) to add a get request which returns all notes. We should declare a DBSession and use it to query the DB for all notes.
- We create post request similar way. But in schemas we create NoteInput using pydantic. This NoteInput can be used in the create request in main.py to give a payload structure for the API to expect. If the payload in the request does not match this, then it instantly returns a Bad Request.
- We created update using the same NoteInput payload structure and a note id to grab the existing note. Missing notes errors handled.
- Delete is also created similarly.
- API endpoint configurations are done (CRUD)

#### Handling CORS

- As we are seperating frontend (client) from the backend (server), we would get CORS issue in the browser while trying to access the API. This is a browser feature.
- CORS is Cross Origin Resource Sharing
- Generally, the API can only be used if the frontend is running on the same domain. Hence to fetch data from another domain, we need to include that domain in the server side.
- Hence we will add CORS middleware in main.py too.
- ```python
  from fastapi.middleware.cors import CORSMiddleware
  ```

Latest Update:

- Need to check what package the guide is recommending to host the API locally to test. Is it uvicorn?
- We do need uvicorn to run and test the server locally. Uvicorn is an AGSI

  AGSI is Asynchronous Gateway Server Interface helps client to communicate with the API.

- install uvicorn standard for more than just bare minimum of the package
- ```bash
  pip install "uvicorn[standard]"
  ```
- Ran the API using `uvicorn main:app --reload` and used [http://127.0.0.1:8000/docs](<[http://127.0.0.1:8000/docs]()>) to test the API in swagger docs.

**The backend part is successfully done for now. Let us build the front end**
