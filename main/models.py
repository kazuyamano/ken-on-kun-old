from main import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta, timezone

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jcode = db.Column(db.String)
    temp = db.Column(db.Float)
    date = db.Column(db.DateTime)

    def __repr__(self):
        return "<Entry id={} jcode={!r} temp={!r} date={}>".format(self.id, self.jcode, self.temp, self.date)


def init():
    db.create_all()
