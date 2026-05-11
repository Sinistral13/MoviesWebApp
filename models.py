from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    """
    Represents a user in the MovieWeb application.

    Each user can have multiple favorite movies associated with them.

    Attributes:
        id (int): Primary key identifier for the user.
        name (str): The user's display name (required).

    Relationships:
        movies (Movie): One-to-many relationship with Movie model
        via Movie.user_id foreign key.
    """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Movie(db.Model):
    """
    Represents a movie saved in a user's favorites list.

    Each movie belongs to exactly one user and stores metadata
    retrieved from the OMDb API.

    Attributes:
        id (int): Primary key identifier for the movie.
        title (str): Movie title.
        director (str): Director of the movie.
        year (int): Release year of the movie.
        poster_url (str): URL to movie poster image.
        user_id (int): Foreign key linking movie to a User.

    Relationships:
        user (User): Many-to-one relationship to the User model.
    """
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    poster_url = db.Column(db.String(100), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('user_id', 'title', name='uq_user_movie_title'),
    )
