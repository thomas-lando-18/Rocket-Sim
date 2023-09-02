from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flasgger import (
    Swagger,
    swag_from,
)
import psycopg2

stinger = Flask("__name__")
stinger.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://stingeradmin:stingeradmin@localhost/stingerdb'
db = SQLAlchemy(stinger)
swagger = Swagger(stinger)

@stinger.route("/", methods=["GET"])
# @swag_from("swagger/main.yml")
def heartbeat():
    """
    This is an endpoint that says hello :)

    Should only be used to check that the application is running correctly.

    """

    return "Hello"

@stinger.route("/about", methods=["GET"])
def about_me():
    """
    Returns a description of what the appplication does.  
    """

    # TODO Remake this using a some sort of JSON or something.
    return "I handle the data and resource managment for the flight crew software group"

@stinger.route('/check_db_connection/user/<username>/passwd/<password>/database/<db>')
def check_db_connection(username, password, db):
    try:
        connection = psycopg2.connect(
            host="localhost",
            database=f"{db}",
            user=f"{username}",
            password=f"{password}"
        )
        return jsonify({"message": "Connected to PostgreSQL"})
    except Exception as e:
        return jsonify({"message": f"Error connecting to PostgreSQL: {str(e)}"})
    

