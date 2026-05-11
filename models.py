from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
    def __init__(self, name):
        """
        Overrides standard constructor.
        Check for name input.
        Remove extra spaces and standardize capitalization.
        """
        if not name:
            raise ValueError("A user name is mandatory!")
        self.name = name.strip().title()
    
    
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    director = db.Column(db.String(100), nullable=False) 
    year = db.Column(db.Integer, nullable=False) 
    poster_url = db.Column(db.String(100), nullable=False) 

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)