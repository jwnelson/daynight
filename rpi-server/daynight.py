#!/bin/env/python3
import threading
import json
import os

import requests
import logging
import datetime

SUNRISE_API = "https://api.sunrise-sunset.org/json"
LATITUDE = 34.0522
LONGITUDE = 118.2437

UPDATE_TIME = 

class DaynightThread(threading.Thread):

	def __init__(self, name = "DaynightThread", daemon = True, daemon = True, lat, lon, update_rate = 12):
		self.lat = lat
		self.lon = lon
		self.update_rate = update_rate # how often (in hours) we should check for time updates


		self.pid = os.getpid()
		self.pidfname = './daynight.pid'
		self.runthread = True	# Used to stop thread if error occurs. run() will check this to see if it should continue execution.

		self.sunrise = None
		self.sunset = None
		self.twilight_begin = None # Nautical twilight
		self.twilight_end = None
		self.last_update = datetime.datetime(1970,1,1) # epoch time (Jan 1, 1970)

	def start(self):
		# setup logging

		# write a pidfile
		with open(pidfname, w) as pidfile:
			pidfile.write(self.pid)
		except IOError as e:
			logging.error("Unable to access or create %s. Ending thread." %self.pidfname)
			self.runthread = False

	def run(self):
		"""
			Main process loop. Check for new sunrise and sunset times everyday, then initiate sunrise
			or sunset sequences.
		"""
		while True:
			if self.runthread = False:
				self.warning("Run flag set to false. Stopping daynight daemon.")
				return

			# update sunrise and sunset times
			current_time = datetime.datetime.now()
			update_timedelta = current_time - self.last_update

			# Update times only if it's been longer than $update_rate hours
			if update_timedelta.seconds/3600 > self.update_rate:
				date = current_time.strftime("%Y-%m-%d")
				response = get_sunset_sunrise_times(LATITUDE, LONGITUDE, date)

				if response is not None:
					if  response["status"] is "OK":
						times = response["results"]

						self.sunrise = times["sunrise"]
						self.sunset = times["sunset"]
						self.twilight_begin = times["nautical_twilight_begin"]
						self.twilight_end = times["nautical_twilight_end"]

						self.last_update = current_time()

					else:
						logging.error("API request error: %s" %response["status"])
						return

			# check if we should begin the sunset sequence
			# check if we should begin the sunrise sequence
				

	def get_sunset_sunrise_times(self, date):
		"""
			Makes a GET request to the sunrise-sunset API and returns a python dict of the parsed JSON response if successful,
			otherwise it returns None.
		"""
		rson = None
		payload = {"lat": self.lat, "lng": self.lon, "date": date}
		try:
			response = requests.get(SUNRISE_API, params=payload)
		except ConnectionError as conerr:
			logging.error(conerr)
			logging.error("Could not connect to sunrise-sunset API. You should probably plug that network cable back in.")
			return None
		
		except requests.excpetions.RequestExcpetion as e:
			logging.error(e)
			return None

		try:
			rson = json.loads(response)
		except ValueError as e:
			logging.error(e)
			logging.error("Couldn't decode JSON from sunset-sunrise API")
			return None

		return rson

	def format_date(self, date):
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

def run_daynight():
	dnthread = DaynightThread(name = "daynight_daemon", daemon = True)
	dnthread.start()


if __name__ == "__main__":
	run_daynight()