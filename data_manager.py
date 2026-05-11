from models import db, User, Movie

class DataManager():


    def create_user(self, name):
        """Create a new user and save it in the database."""
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()


    def get_users(self):
        """Return all users from the database."""
        return User.query.all()


    def get_movies(self, user_id):
       """Return all movies of a specific user."""
       query = query.filter_by(nameuser_id=user_id)
       return query

    def add_movie(self, movie):
        """Add a new movie to a user's favorites."""
        db.session.add(movie)
        db.session.commit()


    def update_movie(self, movie_id, new_title):
        """Update the title of a specific movie."""
        movie = Movie.query.get(movie_id)

        if movie:
            movie.title = new_title
            db.session.commit()
        else:
            print(f'Movie with id "{movie_id}" not found.')


    def delete_movie(self, movie_id):
        """Delete a movie from the database."""
        movie = Movie.query.get(movie_id)

        if movie:
            db.session.delete(movie)
            db.session.commit()
        else:
            print(f'Movie with id "{movie_id}" not found.')
    
        


