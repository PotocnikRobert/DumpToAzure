import time
import sys
import socket
from azure.servicebus import ServiceBusService


key_name = "key_name";
key_value = "key";

sbs = ServiceBusService("flightdata",shared_access_key_name=key_name, shared_access_key_value=key_value);

#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 30003
BUFFER_SIZE = 1024

while(True):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	data = s.recv(BUFFER_SIZE)
	s.close()
	
	msg = str(data)
	msg = msg[2:]
	msg = msg[:-5]
	list = msg.split(",")
	result = ""
	result += "{"
	result += '"MessageType": "'
	result += list[0]
	result += '", '
	result += '"TransmissionType": "'
	result += list[1]
	result += '", '
	result += '"SessionID": "'
	result += list[2]
	result += '", '
	result += '"AircraftID": "'
	result += list[3]
	result += '", '
	result += '"HexIdent": "'
	result += list[4]
	result += '", '
	result += '"FlightID": "'
	result += list[5]
	result += '", '
	result += '"GeneratedDate": "'
	result += list[6]
	result += '", '
	result += '"GeneratedTime": "'
	result += list[7]
	result += '", '
	result += '"LoggedDate": "'
	result += list[8]
	result += '", '
	result += '"LoggedTime": "'
	result += list[9]
	result += '", '
	result += '"CallSign": "'
	result += list[10]
	result += '", '
	result += '"Altitude": "'
	result += list[11]
	result += '", '
	result += '"GroundSpeed": "'
	result += list[12]
	result += '", '
	result += '"Track": "'
	result += list[13]
	result += '", '
	result += '"Latitude": "'
	result += list[14]
	result += '", '
	result += '"Longitude": "'
	result += list[15]
	result += '", '
	result += '"VerticalRate": "'
	result += list[16]
	result += '", '
	result += '"Squawk": "'
	result += list[17]
	result += '", '
	result += '"AlertSqCh": "'
	result += list[18]
	result += '", '
	result += '"Emergency": "'
	result += list[19]
	result += '", '
	result += '"SPI": "'
	result += list[20]
	result += '", '
	result += '"IsOnGround": "'
	result += list[21]
	result += '" '
	result += "}"
	print(result)
	sbs.send_event('radardata', result)