import os
from flask import Flask, render_template, request, redirect
from models import db
from data_fetcher import fetch_data
from data_manager import DataManager

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = (
               f"sqlite:///{os.path.join(basedir, 'data', 'movies.sqlite')}"
               )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

data_manager = DataManager()


@app.route("/", methods=["GET"])
def index():
    """
    The home page of your application.
    Show a list of all registered users
    and a form for adding new users.
    """
    users = data_manager.get_users()
    return render_template("index.html", users=users)


@app.route("/users", methods=["POST"])
def add_user():
    """
    Read data from form.
    Create a new user with the data
    and save it to database.
    """
    name = request.form.get("name")

    if name:
        data_manager.create_user(name)

    return redirect("/")


@app.route("/users/<int:user_id>/movies", methods=["GET"])
def get_user_movies(user_id):
    """Retrieve and display specific user’s list of favorite movies."""
    user = data_manager.get_user(user_id)
    movies = data_manager.get_movies(user_id)
    return render_template("movies.html", user=user, movies=movies)


@app.route("/users/<int:user_id>/movies", methods=["POST"])
def add_movie(user_id):
    """
    Check for movie on www.omdbapi.com.
    If found, passes it to the datamanager
    for saving to database.
    """
    title = request.form.get("title")

    #redundant in this structure, kept for scaling
    if not title:
        return render_template(
                    "error.html",
                    message="Missing Title."
                    ), 400

    movie_data = fetch_data(title)

    if not movie_data:
        return render_template(
                    "error.html",
                    message="Movie not Found!"
                    ), 404

    if data_manager.movie_exists(movie_data, user_id):
        return render_template(
                    "error.html",
                    message="Movie already in favorites for this user!"
                    ), 409

    data_manager.add_movie(movie_data, user_id)

    return redirect(f"/users/{user_id}/movies")

@app.route("/users/<int:user_id>/movies/<int:movie_id>/update", methods=["POST"])
def update_movie(user_id, movie_id):
    """Update the title of a specific movie."""
    new_title = request.form.get("title")
    data_manager.update_movie(movie_id, new_title)

    return redirect(f"/users/{user_id}/movies")


@app.route("/users/<int:user_id>/movies/<int:movie_id>/delete", methods=["POST"])
def delete_movie(user_id, movie_id):
    """Delete specific movie from database."""
    data_manager.delete_movie(movie_id)

    return redirect(f"/users/{user_id}/movies")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True, port=5000)
