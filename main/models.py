from main import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta, timezone

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jcode = db.Column(db.String)
    temp = db.Column(db.Float)
    date = db.Column(db.DateTime)
    breathlessness = db.Column(db.String)
    dullness = db.Column(db.String)
    comment = db.Column(db.String)

    def __repr__(self):
        return "<Entry id={} jcode={!r} temp={!r} date={} breathlessness={!r} dullness={!r} comment={!r}>"\
            .format(self.id, self.jcode, self.temp, self.date, self.breathlessness, self.dullness, self.comment)


def init():
    db.create_all()
