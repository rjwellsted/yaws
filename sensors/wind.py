#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  sensors/wind.py
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
from sensors import i2cbus, pcf8574_address
import smbus

direction = {
     0:None,    1:121.6,  2:182.4,  3:114.0,  4:243.2,  5:129.2,
     6:174.8,   7:167.2,  8:304.0,  9:None,  10:190.0,  11:197.6,
    12:235.6,  13:None,  14:228.0, 15:205.2, 16:0.0,   17:7.6,
    18:None,   19:None,  20:250.8, 21:None,  22:258.4, 23:159.6,
    24:296.4,  25:15.2,  26:None,  27:None,  28:288.8, 29:281.2,
    30:266.0,  31:273.6, 32:60.8,  33:53.2,  34:68.4,  35:106.4,
    36:None,   37:136.8, 38:None,  39:144.4, 40:311.6, 41:None,
    42:None,   43:98.8,  44:319.2, 45:None,  46:220.4, 47:212.8,
    48:357.2,  49:45.6,  50:76.0,  51:83.6,  52:None,  53:38.0,
    54:None,   55:152.0, 56:349.6, 57:22.8,  58:342.0, 59:91.2,
    60:326.8,  61:30.4,  62:334.4, 63:None
}
def __init__():
    b = smbus.SMBus(i2cbus)
    b.write_byte(pcf8574_address, 0xff)

def read_wind():
    return (None, None)
