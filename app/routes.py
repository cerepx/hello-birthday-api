"""
Defines the API routes for the Hello Birthday API.
Includes endpoints for saving users and returning birthday messages.
"""

import re
from datetime import date, datetime
from flask import abort, jsonify, request
from app.models import init_db, save_user_to_db, get_user_from_db


# Initialize the SQLite database (creates table if not exists)
init_db()

def register_routes(app):
    """
    Register all API routes (endpoints) directly to the app.
    """
    def validate_username(username: str) -> None:
        """
        Validates that the username contains only alphabetic characters.
        If invalid, aborts with 400 Bad Request.

        Args:
            username (str): The username to validate.
        """
        if not re.fullmatch(r"[A-Za-z]+", username):
            abort(400, description="Invalid username. Only letters allowed.")


    def validate_date_of_birth(dob: str) -> date:
        """
        Validates that the date of birth is in YYYY-MM-DD format and is before today.
        Returns a date object if valid, else aborts with 400 Bad Request.

        Args:
            dob (str): The date of birth string to validate.

        Returns:
            date: Parsed date object if valid.
        """
        try:
            dob_date = datetime.strptime(dob, "%Y-%m-%d").date()
            if dob_date >= date.today():
                abort(400, description="dateOfBirth must be before today")
            return dob_date
        except ValueError:
            abort(400, description="Invalid date format. Use YYYY-MM-DD.")


    @app.route('/hello/<username>', methods=['PUT'])
    def save_user(username: str) -> tuple[str, int]:
        """
        Saves or updates the user's date of birth.

        Path Args:
            username (str): The username (only alphabetic characters allowed).

        Returns:
            Empty response with 204 No Content on success.
        """
        validate_username(username)

        data = request.get_json()
        if not data or "dateOfBirth" not in data:
            abort(400, description="Missing dateOfBirth in request")

        dob = validate_date_of_birth(data["dateOfBirth"])
        save_user_to_db(username, dob.isoformat())  # Save as ISO string (YYYY-MM-DD)

        return '', 204


    @app.route('/hello/<username>', methods=['GET'])
    def get_birthday_message(username: str):
        """
        Returns a birthday greeting for the given user.

        Path Args:
            username (str): The username.

        Returns:
            JSON with a greeting message or 404 if user not found.
        """
        validate_username(username)

        row = get_user_from_db(username)
        if not row:
            abort(404, description="User not found in the database")

        dob = row[0]
        today = date.today()

        # Replace year to calculate next birthday occurrence
        birthday_this_year = dob.replace(year=today.year)

        # If birthday has already passed this year, calculate for next year
        if birthday_this_year < today:
            next_birthday = birthday_this_year.replace(year=today.year + 1)
        else:
            next_birthday = birthday_this_year

        days_until = (next_birthday - today).days

        # Prepare the birthday message
        if days_until == 0:
            message = f"Hello, {username}! Happy birthday!"
        else:
            message = f"Hello, {username}! Your birthday is in {days_until} day(s)"

        return jsonify({"message": message})


    @app.route("/health")
    def health_check():
        """
        Health check endpoint to verify service is up.
        Used by load balancers or deployment platforms.
        """
        return "OK", 200
