# url for this repo
https://github.com/pleabargain/Fast-API-CRUD-App-Live-Stream-Code

# before running " uvicorn main:app --reload "  you need to install sqlalchemy
pip install sqlalchemy


# start the server
```uvicorn main:app --reload```


# to view the DB in VS code
I use the extension: 

## vscode-sqlite


# view the docs
http://127.0.0.1:8000/docs

# add a new todo item
http://127.0.0.1:8000/docs#/default/addItem__post

# see all items in FastAPI
http://127.0.0.1:8000/docs#/default/getitems_table_get

# view as a table
http://127.0.0.1:8000/table

# view as a basic list
http://127.0.0.1:8000/index


# done
* create a jinja template and render the database 'items'
http://127.0.0.1:8000/table

# to do 
* create a template form that takes a new item and adds it to the task database
    * this has proven very difficult :(
* create a search form
* add footers templates/static
* add headers template with favico templates/static
* add css templates/static


# to review
* https://cookiecutter-fastapi.readthedocs.io/en/latest/userguide.html
* https://www.gormanalysis.com/blog/building-and-deploying-rock-paper-scissors-with-python-fastapi-and-deta/

# courses
* https://academy.christophergs.com/courses/fastapi-for-busy-engineers/

# ORIGINAL README : Dennis Ivy FastAPI CRUD App
This is a simple app designed to play around with FastAPI with a basic CRUD app.
The article accompanying the app can be found at https://medium.com/@dennisivy/my-first-crud-app-with-fast-api-74ac190d2dcc and the livestreamed video can be seen at https://www.youtube.com/watch?v=FOZNYBu8u18.

## Installation
In order to run the app, it is recommended you first create and activate a virtual environment:
```bash
python -m venv env 
```

# python3 -m venv env if on an older system where python 2.7
# is the default version used when calling "python"

# Activate Virtual Environment
# Windows
env\Scripts\activate

# Unix-based
source env/bin/activate
```

Once the virtual environment is activated simply run `pip install -r requirements.txt`

## Run the app
There are multiple options available when running the app.
The way you're likely going to want to do it is by running the command
```bash
uvicorn main:app --reload
```

If you would like to choose a specific port (if 8000 is already occupied by another program), then you can run
```bash
uvicorn main:app --reload --port <PORT>
```
where the `<PORT>` is a number of your choosing.
For the rest of the options when running a uvicorn app, visit https://www.uvicorn.org/#command-line-options.