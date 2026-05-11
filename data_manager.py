from models import db, User, Movie


class DataManager():

    def movie_exists(self, movie, user_id):
        """
        Check for user already having the movie
        in his favorites.
        """
        existing_movie = Movie.query.filter_by(
            title=movie.get("Title"),
            user_id=user_id
            ).first()
        return existing_movie


    def create_user(self, name):
        """Create a new user and save it in the database."""
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()


    def get_users(self):
        """Return all users from the database."""
        return User.query.all()


    def get_user(self, user_id):
        """"Return a specific user by id."""
        return User.query.get_or_404(user_id)


    def get_movies(self, user_id):
        """Return all movies of a specific user."""
        return Movie.query.filter_by(user_id=user_id).all()


    def get_movie(self, movie_id):
        """Return specific Movie."""
        return Movie.query.get_or_404(movie_id)


    def add_movie(self, movie_data, user_id):
        """Add a new movie to a user's favorites."""
        movie = Movie(
            title=movie_data.get("Title"),
            director=movie_data.get("Director"),
            year=int(movie_data.get("Year")),
            poster_url=movie_data.get("Poster"),
            user_id=user_id
            )

        db.session.add(movie)
        db.session.commit()


    def update_movie(self, movie_id, new_title):
        """Update the title of a specific movie."""
        movie = Movie.query.get_or_404(movie_id)
        if new_title:
            movie.title = new_title
            db.session.commit()


    def delete_movie(self, movie_id):
        """Delete a movie from the database."""
        movie = Movie.query.get_or_404(movie_id)

        db.session.delete(movie)
        db.session.commit()
