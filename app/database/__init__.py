from flask import g     # g is where you store data while is running
import sqlite3

DATABASE_URL = "main.db" # this is a constant == can not change

def get_db():       #
    db = getattr(g, "_database", None)  #getattr is a python attribute
    if not db: # the same thing as "if db == None"
        db = g._database = sqlite3.connect(DATABASE_URL)
    return db