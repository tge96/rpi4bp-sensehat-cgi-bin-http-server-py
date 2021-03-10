#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()

#<localhost:8000//cgi-bin/data.py?temperature=78.5&humidity=50.9&pressure=28.9&timestamp=06/03/2021%2012:53:26
valTemperature = form.getvalue('temperature')
valHumidity = form.getvalue('humidity')
valPressure = form.getvalue('pressure')
valTimeStamp = form.getvalue('timestamp')

#append data to file
f = open("iot.txt",  'a')
f.write(str(valTemperature)+','+str(valHumidity)+','+str(valPressure)+','+str(valTimeStamp)+'\n')
f.flush()
f.close()

