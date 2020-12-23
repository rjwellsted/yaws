#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  sensors/__init__.py
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
import re, smbus, w1thermsensor
import gpiozero
i2cbus = None

debug = True

# find out which revision of RPi we are running on
#info = open('/proc/cpuinfo')
#for line in info:
#    line = line.rstrip()
#    if re.search('Revision', line):
#        x, x, rev = line.split()
if  gpiozero.pi_info().revision == '0002':
    i2cbus = 0
else:
    i2cbus = 1

# BME280 Temperature, Pressure & Humidity sensor
_bme280_probe_ = [0x76, 0x77]
bme280_address = None

# BH1750 Ambient light level sensor
_bh1750_probe_ = [0x5c, 0x23]
bh1750_address = None

# PCF8574 8 pin I/O device (wind direction sensor)
_pcf8574_probe_ = [0x20, 0x21, 0x22, 0x24, 0x25, 0x26, 0x27]
pcf8574_address = None

if i2cbus is not None:
    bus = smbus.SMBus(i2cbus)

    for device in _bme280_probe_:
        try:
            bus.read_byte(device)
            bme280_address = device
        except: # exception if read_byte fails
            pass
    for device in _bh1750_probe_:
        try:
            bus.read_byte(device)
            bh1750_address = device
        except: # exception if read_byte fails
            pass
    for device in _pcf8574_probe_:
        try:
            bus.read_byte(device)
            pcf8574_address = device
        except: # exception if read_byte fails
            pass

if debug:
    if i2cbus is not None:
        print('i2cbus=',i2cbus)
        if bme280_address is not None:
            print('bme280=', hex(bme280_address)) 
        else:
            print('bme280 not found')
        if bh1750_address is not None:
            print('bh1750=', hex(bh1750_address)) 
        else:
            print('bh1750 not found')
        if pcf8574_address is not None:
            print('pcf8574=', hex(pcf8574_address))
        else:
            print('pcf8574 not found')
    else:
        print('i2cbus not found, i2c sensors not availabe')
# end of if debug
