# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure import eventhub
from azure.eventhub import EventData, EventHubClient, Offset

import logging
logger = logging.getLogger('azure.eventhub')

import db, json, time, datetime


def get_time():
	cntime = datetime.datetime.now() + datetime.timedelta(hours = +8)
	
	date = cntime.strftime('%Y-{}-{}').format(cntime.strftime('%m').zfill(2), cntime.strftime('%d').zfill(2))
	
	hour = cntime.strftime('%H').zfill(2)
	minute = cntime.strftime('%M').zfill(2)
	second = cntime.strftime('%S').zfill(2)
	
	return [date, hour, minute, second]


def get_iothub_data():
	list = ['0'] * 11
	
	client = EventHubClient.from_iothub_connection_string('<your_connection_string>', debug=True)
	receiver = client.add_receiver("$default", "3", operation='/messages/events', offset = Offset(datetime.datetime.utcnow()))
	
	try:
		client.run()
		eh_info = client.get_eventhub_info()
		print(eh_info)
		
		received = receiver.receive(timeout=5)
		print(received)
		
		for item in received: 
			message = json.loads(str(item.message))
			print(message)
			
			if 'data' in message:
				data = message['data']
				
				air_temp = str(int(data[0:2], 16))
				air_hum = str(int(data[2:4], 16))
				pressure = str(int((data[4:8]), 16))
				co2 = str(int(data[8:12], 16))
				dust = str(int(data[12:16], 16))
				illumination = str(int(data[16:20], 16))
				o2 = str(round(int(data[20:22], 16) / 10, 1))
				soil_temp = str(int(data[22:24], 16))
				soil_hum = str(int(data[24:26], 16))
				voltage = str(round(int(data[26:28], 16) / int('ff', 16) * 5, 1))
				error = str(int(data[28:], 16))
				
				list = [air_temp, air_hum, pressure, co2, dust, illumination, o2, soil_temp, soil_hum, voltage, error]
	
	finally:
		client.stop()
	
	return list


while True:
	list = get_time() + get_iothub_data()
	db.insert(list)
	print(list)
