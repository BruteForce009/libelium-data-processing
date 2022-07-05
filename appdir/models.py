from datetime import datetime
from appdir import db


def remove(string):
    return string.replace(" ", "|")


class SensorData(db.Model):
    NodeID = db.Column(db.String(30), nullable=True, unique=False)
    pm1 = db.Column(db.Float(precision=2), nullable=True, unique=False)
    pm2 = db.Column(db.Float(precision=2), nullable=True, unique=False)
    pm3 = db.Column(db.Float(precision=2), nullable=True, unique=False)
    am = db.Column(db.Float(precision=2), nullable=True, unique=False)
    twd = db.Column(db.String(30), nullable=True, unique=False)
    sm1 = db.Column(db.Float(precision=2), nullable=True, unique=False)
    sm2 = db.Column(db.Float(precision=2), nullable=True, unique=False)
    st = db.Column(db.Float(precision=2), nullable=True, unique=False)
    lum = db.Column(db.Float(precision=2), nullable=True, unique=False)
    temp = db.Column(db.Float(precision=2), nullable=True, unique=False)
    humd = db.Column(db.Float(precision=2), nullable=True, unique=False)
    pres = db.Column(db.Float(precision=2), nullable=True, unique=False)
    bat = db.Column(db.Float(precision=2), nullable=True, unique=False)
    ttime = db.Column(db.String(30), primary_key=True, default=remove(f'{datetime.utcnow()}'))

    def __repr__(self):
        return f"{self.NodeID} {self.pm1} {self.pm2} {self.pm3} {self.am} {self.twd} {self.sm1} {self.sm2} {self.st} {self.lum} {self.temp} {self.humd} {self.pres} {self.bat} {self.ttime}"
