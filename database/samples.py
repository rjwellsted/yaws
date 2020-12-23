#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  database/samples.py
#
#  Copyright 2020 Ron Wellsted <ron@wellsted.org.uk>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

from sqlalchemy import create_engine

engine = create_engine('sqlite:///yaws.sqlite3', echo=True)
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
import datetime
from sqlalchemy import Table, Column, DateTime, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base

def create_connection():
    return engine.connect()

Base = declarative_base()

class Samples(Base):
    __tablename__ = 'samples'
    sampled = Column(DateTime, primary_key=True, default=datetime.datetime.utcnow)
    airtemp = Column(Float)
    gndtemp = Column(Float)
    pressure = Column(Float)
    humidity = Column(Float)
    windspeed = Column(Float)
    direction = Column(Float)
    rain = Column(Boolean)
    rainfall = Column(Float)
    sunlight = Column(Float)
    cputemp = Column(Float)

    def __repr__(self):
        return {'sampled':self.sampled, 'airtemp':self.airtemp,
            'gndtemp':self.gndtemp, 'pressure':self.pressure,
            'humidity':self.humidity, 'windspeed':self.windspeed,
            'rain':self.rain, 'rainfall':self.rainfall,
            'sunlight':self.sunlight, 'cputemp':self.cputemp}

    def __str__(self):
        return (f'Sampled={self.sampled}\n'
            f'AirTemp={self.airtemp}\n'
            f'GndTemp={self.gndtemp}\n'
            f'Pressure={self.pressure}\n'
            f'Humidity={self.humidity}\n'
            f'Windspeed={self.windspeed}\n'
            f'Rain={self.rain}\n'
            f'Rainfall={self.rainfall}\n'
            f'Sunlight={self.sunlight}\n'
            f'CPUTemp={self.cputemp}')

Base.metadata.create_all(engine)
