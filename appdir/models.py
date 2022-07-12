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
    sm = db.Column(db.Float(precision=2), nullable=True, unique=False)
    st = db.Column(db.Float(precision=2), nullable=True, unique=False)
    lum = db.Column(db.Float(precision=2), nullable=True, unique=False)
    temp = db.Column(db.Float(precision=2), nullable=True, unique=False)
    humd = db.Column(db.Float(precision=2), nullable=True, unique=False)
    pres = db.Column(db.Float(precision=2), nullable=True, unique=False)
    lat = db.Column(db.Float(precision=2), nullable=True, unique=False)
    NSI = db.Column(db.String(30), nullable=True, unique=False)
    long = db.Column(db.Float(precision=2), nullable=True, unique=False)
    EWI = db.Column(db.String(30), nullable=True, unique=False)
    alt = db.Column(db.Float(precision=2), nullable=True, unique=False)
    bat = db.Column(db.Float(precision=2), nullable=True, unique=False)
    ttime = db.Column(db.String(30), primary_key=True, default=remove(f'{datetime.utcnow()}'))
    rtctime = db.Column(db.Integer, nullable=True, unique=False, default=404)

    def __repr__(self):
        return f"{self.NodeID} {self.pm1} {self.pm2} {self.pm3} {self.am} {self.twd} {self.sm} {self.st} {self.lum} {self.temp} {self.humd} {self.pres} {self.lat} {self.NSI} {self.long} {self.EWI} {self.alt} {self.bat} {self.ttime}"
