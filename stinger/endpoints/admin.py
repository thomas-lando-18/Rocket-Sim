from flask import Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2


admin_endpoints = Blueprint("admin", __name__)

@admin_endpoints.route("/", methods=["GET"])
def helloe_there():
    """
    This is an endpoint that says hello :)

    Should only be used to check that the application is running correctly.

    """

    return "Hello"


@admin_endpoints.route("/about", methods=["GET"])
def about_me():
    """
    Returns a description of what the appplication does.
    """

    # TODO Remake this using a some sort of JSON or something.
    return "I handle the data and resource managment for the flight crew software group"


@admin_endpoints.route("/check_db_connection/user/<username>/passwd/<password>/database/<db>")
def check_db_connection(username, password, db):
    try:
        connection = psycopg2.connect(
            host="localhost",
            database=f"{db}",
            user=f"{username}",
            password=f"{password}",
        )
        return jsonify({"message": "Connected to PostgreSQL"})
    except Exception as e:
        return jsonify({"message": f"Error connecting to PostgreSQL: {str(e)}"})