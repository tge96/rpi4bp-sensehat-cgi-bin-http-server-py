# rpi4bp-sensehat-cgi-http-server-py

This is the server side collecting data for the sense-hat that is attached to the client (rpi3bp in my case).

iot.txt is local csv formatted data logging file written via /home/pi/cgi-bin/data.py script by the client (rpi3bp in my case).  See rpi3bp-sensehat-cgi-bin-http-client-py repo.

CGIHTTPServer.py is Python2.7 example script.  This script needs to be running on your server (rpi4bp in my case) before you can send data via your client (rpi3bp in my case).

$ python -m CGIHTTPServer.py
