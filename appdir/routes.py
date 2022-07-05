from flask import render_template, url_for, flash, redirect, get_flashed_messages, request
from appdir import app, db
import appdir.models
from datetime import datetime
import math
import json
import time


def remove(string):
    return string.replace(" ", "|")


@app.route('/')
@app.route("/data_")
def data_():
    page = request.args.get('page', 1, type=int)
    sensors = appdir.models.SensorData.query.order_by(appdir.models.SensorData.ttime.desc()).paginate(page=page, per_page=12)
    ttl = math.floor(sensors.total/12 + 1)
    return render_template('data_.html', sensors=sensors, ttl=ttl)


@app.route("/data", methods=['POST'])
def data():
    if request.method == 'POST':
        NodeID = request.args.get('NodeID', type=str)
        pm1 = request.args.get('pm1', type=str)
        pm2 = request.args.get('pm2', type=str)
        pm3 = request.args.get('pm3', type=str)
        am = request.args.get('am', type=str)
        twd = request.args.get('twd', type=str)
        sm1 = request.args.get('sm1', type=str)
        sm2 = request.args.get('sm2', type=str)
        st = request.args.get('st', type=str)
        lum = request.args.get('lum', type=str)
        temp = request.args.get('temp', type=str)
        humd = request.args.get('humd', type=str)
        pres = request.args.get('pres', type=str)
        bat = request.args.get('bat', type=float)
        ttime = request.args.get('ttime', type=str)

        sensordata = appdir.models.SensorData(NodeID=NodeID, pm1=pm1, pm2=pm2, pm3=pm3, am=am, twd=twd, sm1=sm1, sm2=sm2, st=st, lum=lum, temp=temp, humd=humd, pres=pres, bat=bat, ttime=ttime)
        db.session.add(sensordata)
        db.session.commit()
    return 'Done'


@app.route("/datg", methods=['POST'])
def datg():
    NodeID = request.args.get('NodeID', type=str)
    pm1 = request.args.get('pm1', type=str)
    pm2 = request.args.get('pm2', type=str)
    pm3 = request.args.get('pm3', type=str)
    am = request.args.get('am', type=str)
    twd = request.args.get('twd', type=str)
    sm1 = request.args.get('sm1', type=str)
    sm2 = request.args.get('sm2', type=str)
    st = request.args.get('st', type=str)
    lum = request.args.get('lum', type=str)
    temp = request.args.get('temp', type=str)
    humd = request.args.get('humd', type=str)
    pres = request.args.get('pres', type=str)
    bat = request.args.get('bat', type=float)
    ttime = request.args.get('ttime', type=str)

    sensordata = appdir.models.SensorData(NodeID=NodeID, pm1=pm1, pm2=pm2, pm3=pm3, am=am, twd=twd, sm1=sm1, sm2=sm2, st=st, lum=lum, temp=temp, humd=humd, pres=pres, bat=bat, ttime=ttime)
    db.session.add(sensordata)
    db.session.commit()
    return 'Done'


@app.route("/jsondata", methods=['POST'])
def jsondata():
    request_data = request.get_json()

    NodeID = request_data['NodeID']
    pm1 = float(request_data['pm1'])
    pm2 = float(request_data['pm2'])
    pm3 = float(request_data['pm3'])
    am = float(request_data['am'])
    twd = request_data['twd']
    sm1 = float(request_data['sm1'])
    sm2 = float(request_data['sm2'])
    st = float(request_data['st'])
    lum = float(request_data['lum'])
    temp = float(request_data['temp'])
    humd = float(request_data['humd'])
    pres = float(request_data['pres'])
    bat = float(request_data['bat'])
    ttime = request_data['ttime']

    sensordata = appdir.models.SensorData(NodeID=NodeID, pm1=pm1, pm2=pm2, pm3=pm3, am=am, twd=twd, sm1=sm1, sm2=sm2, st=st, lum=lum, temp=temp, humd=humd, pres=pres, bat=bat, ttime=ttime)
    db.session.add(sensordata)
    db.session.commit()
    return 'Done'


@app.route("/newjsondata", methods=['POST'])
def newjsondata():
    request_data = request.get_json()
    ttime = remove(f'{datetime.utcnow()}')
    if request_data:
        if 'NodeID' in request_data:
            NodeID = request_data['NodeID']
        if 'pm1' in request_data:
            pm1 = float(request_data['pm1'])
        if 'pm2' in request_data:
            pm2 = float(request_data['pm2'])
        if 'pm3' in request_data:
            pm3 = float(request_data['pm3'])
        if 'am' in request_data:
            am = float(request_data['am'])
        if 'twd' in request_data:
            twd = request_data['twd']
        if 'sm1' in request_data:
            sm1 = float(request_data['sm1'])
        if 'sm2' in request_data:
            sm2 = float(request_data['sm2'])
        if 'st' in request_data:
            st = float(request_data['st'])
        if 'lum' in request_data:
            lum = float(request_data['lum'])
        if 'temp' in request_data:
            temp = float(request_data['temp'])
        if 'humd' in request_data:
            humd = float(request_data['humd'])
        if 'pres' in request_data:
            pres = float(request_data['pres'])
        if 'bat' in request_data:
            bat = float(request_data['bat'])
        if 'ttime' in request_data:
            ttime = request_data['ttime']

        sensordata = appdir.models.SensorData(NodeID=NodeID, pm1=pm1, pm2=pm2, pm3=pm3, am=am, twd=twd, sm1=sm1, sm2=sm2, st=st, lum=lum, temp=temp, humd=humd, pres=pres, bat=bat, ttime=ttime)
        db.session.add(sensordata)
        db.session.commit()
    return 'Done'
