#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  sensors/tph.py
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
import smbus2
import bme280
from sensors import i2cbus, bme280_address
import w1thermsensor

def __init__():
    if bme280_address is not None:
        bus = smbus2.SMBus(i2cbus)
        calibration_params = bme280.load_calibration_params(bus, bme280_address)
        data = bme280.sample(bus, bme280_address, calibration_params)

def read_tph():
    if bme280_address is not None:
        data = bme280.sample(bus, bme280_address, calibration_params)
        air_temp = data.temperature
        pressure  = data.pressure/1000.0 # convert to Bar
        humidity  = data.humidity
    else:
        air_temp = None
        pressure = None
        humidity = None
    return (air_temp, pressure, humidity)

