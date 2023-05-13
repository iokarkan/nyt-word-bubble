from . import db

# SQLAlchemy model for the word frequency table
class WordFrequencyWeek(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(30))
    frequency = db.Column(db.Integer)


class WordFrequencyDay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(30))
    frequency = db.Column(db.Integer)
