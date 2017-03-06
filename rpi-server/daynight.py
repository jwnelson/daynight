#!/bin/env/python3
import threading

import requests
import logging
import time

SUNRISE_API = "https://api.sunrise-sunset.org/json"
LATITUDE = 34.0522
LONGITUDE = 118.2437

UPDATE_TIME = 

def format_date(date):
	"""
		Format the date as a YYY-mm-dd string and zero-pad month and day if necessary.

		Expects a time.struct_time object.
	"""
	year = date.tm_year
	mon = date.tm_mon
	day = date.tm_mday

	if mon < 10:
		mon = "0%d" %mon
	if day < 10:
		day = "0%d" %day

	fdate = "%d-%d-%d" %(year, mon, day)
	return fdate




class DaynightThread(threading.Thread):

	def run():
		"""
			Main process loop. Check for new sunrise and sunset times everyday, then initiate sunrise
			or sunset sequences.
		"""
		while True:
			current_time = time.localtime()
			if current_time.tm_hour = 0:
				date = format_date(current_time)
				times = get_sunset_sunrise_times(LATITUDE, LONGITUDE, date)
				

def get_sunset_sunrise_times(lat, lon, date):
	"""
		Makes a GET request to the sunrise-sunset API and returns the JSON if successful,
		else returns None.
	"""
	rson = None
	payload = {"lat": lat, "lng": lon, "date": date}
	response = requests.get(SUNRISE_API, params=payload)

	try:
		rson = r.json()
	except ValueError as e:
		logging.error("Couldn't decode JSON from sunset-sunrise API\n%s" %e)
		return rson

	return rson

def run_init():
	# setup logging

def run_daynight():
	dnthread = DaynightThread(name = "daynight_daemon", daemon = True)
	dnthread.start()


if __name__ == "__main__":
	run_init()
	run_daynight()