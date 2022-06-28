from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, IntegerField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from appdir.models import SensorData



class PostForm(FlaskForm):
    NodeID = StringField('NodeID')
    pm1 = StringField('tpluviometer1')
    pm2 = StringField('tpluviometer2')
    pm3 = StringField('tpluviometer3')
    am = StringField('tanemometer')
    vane_str = StringField('twd')
    sm = StringField('tSoil_moist')
    temp = StringField('ttemp')
    humd = StringField('thumd')
    pres = StringField('tpres')
    lum = StringField('tLuminosity')
    bat = IntegerField('tbat')
    timex = StringField('ttime')