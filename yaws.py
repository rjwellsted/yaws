#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  yaws.py
#  
#  Copyright 2020 Ron Wellsted <ron@wellsted.org.uk>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
cfgPath = './yaws.cfg'

import database.samples as db
from gpiozero import CPUTemperature
import time
import sensors
from sensors import tph, rain, wind, light

AirTemp = None
GndTemp = None
Pressure = None
Humidity = None
WindSpeed = None
WindDirection = None
Rain =  None
Rainfall = None
Sunlight = None
cpu = None

def main(args):
    conn = db.create_connection()
    while True:
        # get Air tph
        data = tph.read_tph()
        AirTemp = data[0]
        Pressure = data[1]
        Humidity = data[2]
        
        # get Ground temperature
        
        # get Rain info
        data = rain.read_rain()
        Rain = data[0]
        Rainfall = data[1]
        
        # get Wind info
        data = wind.read_wind()
        WindDirection = data[0]
        WindSpeed = data[1]
        
        # get light level
        Sunlight = light.read_light()
        
        # get CPU Temp
        cpu = CPUTemperature()
        
        Sample = db.Samples(airtemp = AirTemp, gndtemp = GndTemp,
            pressure = Pressure, humidity = Humidity, windspeed = WindSpeed,
            direction = WindDirection, rain = Rain, rainfall = Rainfall,
            sunlight = Sunlight, cputemp = float(cpu.temperature))
        db.session.add(Sample)
        db.session.commit()
        time.sleep(60)
    return 0

if __name__ == '__main__':
    import sys, configparser
    # cfg = configparser.ConfigParser()
    # cfg.read(cfgPath)
    # dbPath = cfg['global']['dbPath']
    sys.exit(main(sys.argv))
