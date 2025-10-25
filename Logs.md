# **Logs**

I am going to log my progress

Struggled with getting virtualenvwrapper installed as I had to install it using homebrew and there was an error ("missing double quote") in the .zshrc file.

Installed virtualenvwrapper

FastAPI now runs on venvwrapper called nid_api. use wokon nid_api

Installed fast API

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
