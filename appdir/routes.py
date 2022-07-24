from flask import render_template, url_for, request
from appdir import app, db
import appdir.models
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math
import mpld3


def remove(string):
    return string.replace(" ", "|")


@app.route('/')
@app.route("/reroute")
def reroute():
    return render_template('re-route.html')


@app.route("/data_")
def data_():
    page = request.args.get('page', 1, type=int)
    sensorL = appdir.models.SensorData.query.order_by(appdir.models.SensorData.rtctime.desc()).paginate(page=page, per_page=9)
    ttl = math.floor(sensorL.total/9 + 1)
    return render_template('data_.html', sensorL=sensorL, ttl=ttl)


@app.route("/data_plot")
def data_plot():
    conn = db.engine.connect()
    df = pd.read_sql_table('sensor_data', conn)
    pm1 = df['pm1']
    ttime = df['ttime']
    x_indexes = np.arange(len(ttime))
    plt.figure(1)
    plt.style.use('ggplot')
    plt.plot(x_indexes, pm1, '.-r', label='pm1')
    plt.xlabel('Time')
    plt.ylabel('Rain in the current hour (mm)')
    plt.title('Pluviometer 1')
    plt.grid(True)
    plt.savefig('appdir/static/images/pm1.png')

    return render_template('data_plot.html')


@app.route("/pm2")
def pm2():
    conn = db.engine.connect()
    df = pd.read_sql_table('sensor_data', conn)
    ttime = df['ttime']
    pm2 = df['pm2']
    plt.figure(2)
    plt.style.use('ggplot')
    plt.plot(ttime, pm2, 'x--g', label='pm2')
    plt.xlabel('Time')
    plt.ylabel('Rain in the previous hour (mm)')
    plt.title('Pluviometer 2')
    plt.grid(True)
    
    plt.savefig('appdir/static/images/pm2.png')

    return render_template('pm2.html')


@app.route("/pm3")
def pm3():
    conn = db.engine.connect()
    df = pd.read_sql_table('sensor_data', conn)
    ttime = df['ttime']
    pm3 = df['pm3']
    plt.figure(3)
    plt.style.use('ggplot')
    plt.plot(ttime, pm3, 'x--b', label='pm3')
    plt.xlabel('Time')
    plt.ylabel('Rain in the last 24 hours (mm)')
    plt.title('Pluviometer 3')
    plt.grid(True)
    
    plt.savefig('appdir/static/images/pm3.png')

    return render_template('pm3.html')


@app.route("/anemo")
def anemo():
    conn = db.engine.connect()
    df = pd.read_sql_table('sensor_data', conn)
    ttime = df['ttime']
    am = df['am']
    plt.figure(4)
    plt.style.use('ggplot')
    plt.plot(ttime, am, 'x--r', label='Anemometer')
    plt.xlabel('Time')
    plt.ylabel('Wind Speed (km/h)')
    plt.title('Anemometer')
    plt.grid(True)
    
    plt.savefig('appdir/static/images/am.png')

    return render_template('anemo.html')


@app.route("/sm")
def sm():
    conn = db.engine.connect()
    df = pd.read_sql_table('sensor_data', conn)
    ttime = df['ttime']
    sm = df['sm']
    plt.figure(5)
    plt.style.use('ggplot')
    plt.plot(ttime, sm, 'x--r', label='Soil Moisture')
    plt.xlabel('Soil moisture (centibar)')
    plt.ylabel('Readings')
    plt.title('Watermark')
    plt.grid(True)
    
    plt.savefig('appdir/static/images/sm.png')

    return render_template('sm.html')


@app.route("/st")
def st():
    conn = db.engine.connect()
    df = pd.read_sql_table('sensor_data', conn)
    ttime = df['ttime']
    st = df['st']
    plt.figure(6)
    plt.style.use('ggplot')
    plt.plot(ttime, st, 'x--r', label='Soil Temperature')
    plt.xlabel('Time')
    plt.ylabel('Soil Temperature (°C)')
    plt.title('PT-1000')
    plt.grid(True)
    
    plt.savefig('appdir/static/images/st.png')

    return render_template('st.html')


@app.route("/lum")
def lum():
    conn = db.engine.connect()
    df = pd.read_sql_table('sensor_data', conn)
    ttime = df['ttime']
    lum = df['lum']
    plt.figure(7)
    plt.style.use('ggplot')
    plt.plot(ttime, lum, 'x--r', label='Luminosity')
    plt.xlabel('Time')
    plt.ylabel('Illuminance (lux)')
    plt.title('Luminosity')
    plt.grid(True)
    
    plt.savefig('appdir/static/images/lum.png')

    return render_template('lum.html')


@app.route("/temp")
def temp():
    conn = db.engine.connect()
    df = pd.read_sql_table('sensor_data', conn)
    ttime = df['ttime']
    temp = df['temp']
    plt.figure(8)
    plt.style.use('ggplot')
    plt.plot(ttime, temp, 'x--r', label='Temperature')
    plt.xlabel('Time')
    plt.ylabel('°C')
    plt.title('Temperature')
    plt.grid(True)
    
    plt.savefig('appdir/static/images/temp.png')

    return render_template('temp.html')


@app.route("/humd")
def humd():
    conn = db.engine.connect()
    df = pd.read_sql_table('sensor_data', conn)
    ttime = df['ttime']
    humd = df['humd']
    plt.figure(9)
    plt.style.use('ggplot')
    plt.plot(ttime, humd, 'x--r', label='Humidity')
    plt.xlabel('Time')
    plt.ylabel('%')
    plt.title('humd')
    plt.grid(True)
    
    plt.savefig('appdir/static/images/humd.png')

    return render_template('humd.html')


@app.route("/pres")
def pres():
    conn = db.engine.connect()
    df = pd.read_sql_table('sensor_data', conn)
    ttime = df['ttime']
    pres = df['pres']
    plt.figure(10)
    plt.style.use('ggplot')
    plt.plot(ttime, pres, 'x--r', label='Pressure')
    plt.xlabel('Time')
    plt.ylabel('Pascal')
    plt.title('Pressure')
    plt.grid(True)
    
    plt.savefig('appdir/static/images/pres.png')

    return render_template('pres.html')


@app.route("/jsondata", methods=['POST'])
def jsondata():
    request_data = request.get_json()

    NodeID = request_data['NodeID']
    pm1 = float(request_data['pm1'])
    pm2 = float(request_data['pm2'])
    pm3 = float(request_data['pm3'])
    am = float(request_data['am'])
    twd = request_data['twd']
    sm = float(request_data['sm'])
    st = float(request_data['st'])
    lum = float(request_data['lum'])
    temp = float(request_data['temp'])
    humd = float(request_data['humd'])
    pres = float(request_data['pres'])
    lat = float(request_data['lat'])
    NSI = request_data['NSI']
    long = float(request_data['long'])
    EWI = request_data['EWI']
    alt = float(request_data['alt'])
    bat = float(request_data['bat'])
    ttime = int(request_data['ttime'])

    rtctime = ttime
    new_time = datetime.fromtimestamp(ttime)
    ttime = remove(f'{new_time}')

    sensordata = appdir.models.SensorData(NodeID=NodeID, pm1=pm1, pm2=pm2, pm3=pm3, am=am, twd=twd, sm=sm, st=st, lum=lum, temp=temp, humd=humd, pres=pres, lat=lat, NSI=NSI, long=long, EWI=EWI, alt=alt, bat=bat, ttime=ttime, rtctime=rtctime)
    db.session.add(sensordata)
    db.session.commit()
    return 'Done'


@app.route("/newjsondata", methods=['POST'])
def newjsondata():
    request_data = request.get_json()

    NodeID = 'X'
    pm1 = 1.23
    pm2 = 1.23
    pm3 = 1.23
    am = 1.23
    twd = 'X'
    sm = 1.23
    st = 1.23
    lum = 1.23
    temp = 1.23
    humd = 1.23
    pres = 1.23
    lat = 1.23
    NSI = 'X'
    long = 1.23
    EWI = 'X'
    alt = 1.23
    bat = 1.23

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
        if 'sm' in request_data:
            sm = float(request_data['sm'])
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
        if 'lat' in request_data:
            lat = float(request_data['lat'])
        if 'NSI' in request_data:
            NSI = request_data['NSI']
        if 'long' in request_data:
            long = float(request_data['long'])
        if 'EWI' in request_data:
            EWI = request_data['EWI']
        if 'alt' in request_data:
            alt = float(request_data['alt'])
        if 'bat' in request_data:
            bat = float(request_data['bat'])
        if 'ttime' in request_data:
            ttime = int(request_data['ttime'])
            rtctime = ttime
            new_time = datetime.fromtimestamp(ttime)
            ttime = remove(f'{new_time}')
        else:
            ttime = remove(f'{datetime.utcnow()}')

        sensordata = appdir.models.SensorData(NodeID=NodeID, pm1=pm1, pm2=pm2, pm3=pm3, am=am, twd=twd, sm=sm, st=st, lum=lum, temp=temp, humd=humd, pres=pres, lat=lat, NSI=NSI, long=long, EWI=EWI, alt=alt, bat=bat, ttime=ttime, rtctime=rtctime)
        db.session.add(sensordata)
        db.session.commit()
    return 'Done'
