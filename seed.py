from app import app
from models import db, User, Movie


def seed_database():
    """
    Seeds the database with test users and movies.
    This is intended for one-time development use only.
    """

    print("Seeding database...")

    # Clear existing data (safe for dev only)
    Movie.query.delete()
    User.query.delete()
    db.session.commit()

    # Create users
    users = [
        User(name="Alice"),
        User(name="Bob"),
        User(name="Charlie"),
        User(name="Diana"),
        User(name="Eve"),
        User(name="Frank")
    ]

    db.session.add_all(users)
    db.session.commit()  # generates IDs

    # Create movies (10 films with titles)
    movies = [
        Movie(title="Inception", director="Nolan", year=2010, poster_url="url1", user_id=users[0].id),
        Movie(title="Jurassic Park", director="Spielberg", year=1993, poster_url="url2", user_id=users[1].id),
        Movie(title="Pulp Fiction", director="Tarantino", year=1994, poster_url="url3", user_id=users[2].id),
        Movie(title="The Lord of the Rings", director="Jackson", year=2001, poster_url="url4", user_id=users[3].id),
        Movie(title="Titanic", director="Cameron", year=1997, poster_url="url5", user_id=users[4].id),
        Movie(title="Gladiator", director="Scott", year=2000, poster_url="url6", user_id=users[5].id),
        Movie(title="The Wolf of Wall Street", director="Scorsese", year=2013, poster_url="url7", user_id=users[0].id),
        Movie(title="Dune", director="Villeneuve", year=2021, poster_url="url8", user_id=users[1].id),
        Movie(title="Fight Club", director="Fincher", year=1999, poster_url="url9", user_id=users[2].id),
        Movie(title="Star Wars: A New Hope", director="Lucas", year=1977, poster_url="url10", user_id=users[3].id),
    ]

    db.session.add_all(movies)
    db.session.commit()

    print("Seeding complete!")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed_database()