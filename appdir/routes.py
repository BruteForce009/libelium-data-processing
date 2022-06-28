from flask import render_template, url_for, flash, redirect, get_flashed_messages, request
from appdir import app, db
import appdir.models
import appdir.forms
import json
import time


@app.route('/')
@app.route("/data_")
def data_():
    sensors = appdir.models.SensorData.query.all()
    return render_template('data_.html', sensors=sensors)


@app.route("/data", methods=['POST'])
def data():
    if request.method == 'POST':
        NodeID = request.args.get('NodeID', type=str)
        pm1 = request.args.get('tpluviometer1', type=str)
        pm2 = request.args.get('tpluviometer2', type=str)
        pm3 = request.args.get('tpluviometer3', type=str)
        am = request.args.get('tanemometer', type=str)
        vane_str = request.args.get('twd', type=str)
        sm = request.args.get('tSoil_moist', type=str)
        temp = request.args.get('ttemp', type=str)
        humd = request.args.get('thumd', type=str)
        pres = request.args.get('tpres', type=str)
        lum = request.args.get('tLuminosity', type=str)
        bat = request.args.get('tbat', type=float)
        timex = request.args.get('ttime', type=str)
        sensordata = appdir.models.SensorData(NodeID=NodeID, tpluviometer1=pm1, tpluviometer2=pm2, tpluviometer3=pm3, tanemometer=am, twd=vane_str, tSoil_moist=sm, ttemp=temp, thumd=humd, tpres=pres, tLuminosity=lum, tbat=bat, ttime=timex)
        db.session.add(sensordata)
        db.session.commit()
    sensors = appdir.models.SensorData.query.all()
    return render_template('data_.html', sensors=sensors)


@app.route("/datg", methods=['POST'])
def datg():
    NodeID = request.args.get('NodeID')
    pm1 = request.args.get('tpluviometer1')
    pm2 = request.args.get('tpluviometer2')
    pm3 = request.args.get('tpluviometer3')
    am = request.args.get('tanemometer')
    vane_str = request.args.get('twd')
    sm = request.args.get('tSoil_moist')
    temp = request.args.get('ttemp')
    humd = request.args.get('thumd')
    pres = request.args.get('tpres')
    lum = request.args.get('tLuminosity')
    bat = request.args.get('tbat')
    timex = request.args.get('ttime')
    sensordata = appdir.models.SensorData(NodeID=NodeID, tpluviometer1=pm1, tpluviometer2=pm2, tpluviometer3=pm3, tanemometer=am, twd=vane_str, tSoil_moist=sm, ttemp=temp, thumd=humd, tpres=pres, tLuminosity=lum, tbat=bat, ttime=timex)
    db.session.add(sensordata)
    db.session.commit()
    sensors = appdir.models.SensorData.query.all()
    return render_template('data_.html', sensors=sensors)


@app.route("/datx?NodeID=<NodeID>&tpluviometer1=<pm1>&tpluviometer2=<pm2>&tpluviometer3=<pm3>&tanemometer=<am>&twd=<vane_str>&tSoil_moist=<sm>&ttemp=<temp>&thumd=<humd>&tpres=<pres>&tLuminosity=<lum>&tbat=<int:bat>&ttime=<timex>", methods=['GET', 'POST'])
def datx(NodeID, pm1, pm2, pm3, am, vane_str, sm, temp, humd, pres, lum, bat, timex):
    sensordata = appdir.models.SensorData(NodeID=NodeID, tpluviometer1=pm1, tpluviometer2=pm2, tpluviometer3=pm3, tanemometer=am, twd=vane_str, tSoil_moist=sm, ttemp=temp, thumd=humd, tpres=pres, tLuminosity=lum, tbat=bat, ttime=timex)
    db.session.add(sensordata)
    db.session.commit()
    sensors = appdir.models.SensorData.query.all()
    return render_template('data_.html', sensors=sensors)


@app.route("/jsondata", methods=['POST'])
def jsondata():
    request_data = request.get_json()

    NodeID = request_data['NodeID']
    pm1 = request_data['tpluviometer1']
    pm2 = request_data['tpluviometer2']
    pm3 = request_data['tpluviometer3']
    am = request_data['tanemometer']
    vane_str = request_data['twd']
    sm = request_data['tSoil_moist']
    temp = request_data['ttemp']
    humd = request_data['thumd']
    pres = request_data['tpres']
    lum = request_data['tLuminosity']
    bat = request_data['tbat']
    timex = request_data['ttime']

    sensordata = appdir.models.SensorData(NodeID=NodeID, tpluviometer1=pm1, tpluviometer2=pm2, tpluviometer3=pm3, tanemometer=am, twd=vane_str, tSoil_moist=sm, ttemp=temp, thumd=humd, tpres=pres, tLuminosity=lum, tbat=bat, ttime=timex)
    db.session.add(sensordata)
    db.session.commit()
    sensors = appdir.models.SensorData.query.all()
    return render_template('data_.html', sensors=sensors)
