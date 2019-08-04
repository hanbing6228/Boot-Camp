import pandas as pd
import numpy as np
import datetime as dt

from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station


app = Flask(__name__)

@app.route("/")
def home():
    return (
         f"Available Routes:<br/>"
         f"/api/v1.0/precipitation<br/>"
         f"/api/v1.0/stations<br/>"
         f"/api/v1.0/tobs<br/>"
         f"/api/v1.0/tem/<start><br/>"
         f"/api/v1.0/tem/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    query_date = dt.date(2016, 12, 30) - dt.timedelta(days=365)
    result_prcps = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date > query_date).\
        order_by(Measurement.date).all()
    precipitation = []
    for date, prcp in result_prcps:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["precipition"] = prcp
        precipitation.append(precipitation_dict)
    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    result_station = session.query(Station.name).all()
    all_station = list(np.ravel(result_station))
    return jsonify(all_station)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    query_date = dt.date(2016, 12, 30) - dt.timedelta(days=365)
    result_tobs = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date > query_date).\
        order_by(Measurement.date).all()
    temperature = []
    for date, tobs in result_tobs:
        temperature_dict = {}
        temperature_dict["date"] = date
        temperature_dict["temperature"] = tobs
        temperature.append(temperature_dict)
    return jsonify(temperature)
    
@app.route('/test')
def test():
    return jsonify({'test': 'test'})



def calc_temps(session, start_date, end_date):
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
# @app.route("/api/v1.0/start")

@app.route("/api/v1.0/startalt")
def startalt():

    session = Session(engine)
    start = "2017-01-01"
    end = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    start_d = dt.datetime.strptime(start, '%Y-%m-%d')
    end_d = dt.datetime.strptime(end, '%Y-%m-%d')
    step = dt.timedelta(days=1)
    date1_l = []
    while start_d <= end_d:
        d = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date == start_d.date()).all()
        date1_l.append(*d)
        start_d += step

    return jsonify(date1_l)

@app.route("/api/v1.0/start")
def start():
    session = Session(engine)
    start = "2017-01-01"
    end = "2017-01-10"
    data1 = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date>=start).filter(Measurement.date<=end).all()
    data2 = list(np.ravel(data1))
    return jsonify(data2)


if __name__ == "__main__":
    app.run(debug=True)
