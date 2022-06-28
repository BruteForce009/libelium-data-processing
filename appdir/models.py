from datetime import datetime
from appdir import db


def remove(string):
    return string.replace(" ", "-")


class SensorData(db.Model):
    NodeID = db.Column(db.String(100), nullable=True, unique=False)
    tpluviometer1 = db.Column(db.String(100), nullable=True,unique=False)
    tpluviometer2 = db.Column(db.String(100), nullable=True, unique=False)
    tpluviometer3 = db.Column(db.String(100), nullable=True, unique=False)
    tanemometer = db.Column(db.String(100), nullable=True, unique=False)
    twd = db.Column(db.String(100), nullable=True, unique=False)
    tSoil_moist = db.Column(db.String(100), nullable=True, unique=False)
    ttemp = db.Column(db.String(100), nullable=True, unique=False)
    thumd = db.Column(db.String(100), nullable=True, unique=False)
    tpres = db.Column(db.String(100), nullable=True,unique=False)
    tLuminosity = db.Column(db.String(100), nullable=True, unique=False)
    tbat = db.Column(db.Float(precision=6), nullable=True, unique=False)
    ttime = db.Column(db.String(100), primary_key=True, default=remove(f'{datetime.utcnow()}'))

    def __repr__(self):
        return f"{self.NodeID} {self.tpluviometer1} {self.tpluviometer2} {self.tpluviometer3} {self.tanemometer} {self.twd} {self.tSoil_moist} {self.ttemp} {self.thumd} {self.tpres} {self.tLuminosity} {self.tbat} {self.ttime}"
