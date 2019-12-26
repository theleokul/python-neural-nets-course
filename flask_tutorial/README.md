# How to run this project

## Install dependencies

1. `pip install flask`  -  Flask framework
2. `pip install flask_sqlalchemy`  -  ORM (Utility for databases) for Flask
3. `pip install flask_marshmallow`  -  Sugar for serialization and deserialization procedures
4. `pip install marshmallow-sqlalchemy`  -  Add some connections between **sqlalchemy** and **marshmallow**

## Create sqlite database

`python3 -c “from crud import db; db.create_all()”`  -  Sometimes instead of `python3` you should use `python`

> Upper command will create crud.sqlite file (which is a database) in your working directory (where you are located in terminal).
> So be sure, you are located in flask_tutorial directory.

## Run project

`python3 hello_world.py`  -  Launch **hello_world** web application (Provides endpoint with simple text)  
`python3 crud.py`  -  Launch **crud** web application (App with database, be sure you have crud.sqlite in working directory)

After proccess is launched, copy link from program output and paste it in a **browser** or the **Postman** to get results.
