import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Set up the Database
engine = create_engine('sqlite:///hawaii.sqlite')
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save our references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link
session = Session(engine)

# Set Up Flask
app = Flask(__name__)

# Set up the flask route
@app.route('/')
def welcome():
    return """Welcome to the Climate Analysis API!
              Available Routes:
              /api/v1.0/precipitation
              /api/v1.0/stations
              /api/v1.0/tobs
              /api/v1.0/temp/start/end"""

@app.route('/api/v1.0/precipitation')
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

@app.route('/api/v1.0/stations')
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)