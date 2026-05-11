import os
from flask import Flask
from models import db
from data_fetcher import fetch_data

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/movies.sqlite')}"

db.init_app(app)


@app.route("/", methods=["GET"])
def home():
    """
    The home page of your application. 
    Show a list of all registered users 
    and a form for adding new users.
    """
    users = User.query.all()
    return render_template("home.html", users=users)


@app.route("/users", methods=["POST"])
def add_user():
    """
    Read data from form.
    Create a new user with the data
    and save it to database.
    """
    name = request.form.get("name")

    if name:
        user = User(name=name)
        db.session.add(user)
        db.session.commit()

    return redirect("/")


@app.route("/users/<int:user_id>/movies", methods=["GET"])
def user_movies(user_id):
    """Retrieve and display specific user’s list of favorite movies."""
    user = User.query.get_or_404(user_id)
    return render_template("movies.html", user=user)


@app.route("/users/<int:user_id>/movies", methods=["POST"])
def add_movie(user_id):
    """
    Check for movie on www.omdbapi.com.
    If found, completes the Movie object with the found data
    and saves Movie to the database..
    """
    title = request.form.get("title")

    movie_data = fetch_data(title)

    if not movie_data:
        return "Movie not found", 404

    movie = Movie(
        title=movie_data.get("Title"),
        director=movie_data.get("Director"),
        year=int(movie_data.get("Year")),
        poster_url=movie_data.get("Poster"),
        user_id=user_id
    )

    data_manager.add_movie(movie)

    return redirect(f"/users/{user_id}/movies")


@app.route("/users/<int:user_id>/movies/<int:movie_id>/update", methods=["POST"])
def update_movie(user_id, movie_id):
    """"Update the title of a specific movie."""
    movie = Movie.query.get_or_404(movie_id)

    new_title = request.form.get("title")

    if new_title:
        movie.title = new_title

    db.session.commit()

    return redirect(f"/users/{user_id}/movies")


@app.route("/users/<int:user_id>/movies/<int:movie_id>/delete", methods=["POST"])
def delete_movie(user_id, movie_id):
    """Delete specific movie from database."""
    movie = Movie.query.get_or_404(movie_id)

    db.session.delete(movie)
    db.session.commit()

    return redirect(f"/users/{user_id}/movies")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True, port=5000)