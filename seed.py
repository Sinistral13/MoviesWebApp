from app import app
from models import db, User, Movie


def seed_database():
    print("Seeding database...")

    # Clear existing data (safe for one-time use)
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
    db.session.commit()  # IMPORTANT: generates user IDs

    # Create movies (10 films)
    movies = [
        Movie(director="Nolan", year=2010, poster_url="url1", user_id=users[0].id),
        Movie(director="Spielberg", year=1993, poster_url="url2", user_id=users[1].id),
        Movie(director="Tarantino", year=1994, poster_url="url3", user_id=users[2].id),
        Movie(director="Jackson", year=2001, poster_url="url4", user_id=users[3].id),
        Movie(director="Cameron", year=1997, poster_url="url5", user_id=users[4].id),
        Movie(director="Scott", year=2000, poster_url="url6", user_id=users[5].id),
        Movie(director="Scorsese", year=2013, poster_url="url7", user_id=users[0].id),
        Movie(director="Villeneuve", year=2021, poster_url="url8", user_id=users[1].id),
        Movie(director="Fincher", year=1999, poster_url="url9", user_id=users[2].id),
        Movie(director="Lucas", year=1977, poster_url="url10", user_id=users[3].id),
    ]

    db.session.add_all(movies)
    db.session.commit()

    print("Seeding complete!")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed_database()