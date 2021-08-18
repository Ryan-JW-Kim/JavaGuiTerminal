from datetime import datetime
import time
import cv2

def ring_alarm():
	print("wake")

def sleep_survey():
	return input("Rate out of 10 (0-10)")

def quit(watcher):
	time.sleep(300)
	is_awake = watcher.look()
	
	return is_awake

class Time:

	def __init__(self, hour, minute, second=0):

		self.day = datetime.now().day

		self.hour = hour
		self.minute = minute
		self.second = second

		self.disposable_h = None
		self.disposable_m = None
		self.disposable_s = None

	def _tuple(self):
		return (self.hour, self.minute, self.second)

	def __str__(self):
		return f"{self.hour}:{self.minute}"

	def _delta(self, TimeObj):

		if self.day != TimeObj.day:

			"""
			if self.day > TimeObj.day:

				self.disposable_h = self.hour + 24
				self.disposable_m = self.minute

				TimeObj.disposable_h = TimeObj.hour
				TimeObj.disposable_m = TimeObj.minute

			else:
	

				TimeObj.disposable_h = TimeObj.hour + 24
				TimeObj.disposable_m = TimeObj.minute

				self.disposable_h = self.hour
				self.disposable_m = self.minute
			"""

			dH = (24 - self.hour) + TimeObj.hour

			dM = (60 - self.minute) + TimeObj.minute

		else:

			dH = TimeObj.hour - self.hour
			
			if self.hour > TimeObj.hour:

				dM = (60 - TimeObj.minute) + self.minute

			else:

				dM = (60 - self.minute) + TimeObj.minute

		periodObj = Period(dH, dM)

		return periodObj

	def time_in(self, periodObj):

		h = self.hour + periodObj.hours
		m = self.minute + periodObj.minutes

		while h > 24:
			h -= 24

		while m > 60:
			m -= 60

		return Time(h, m)

	def compare(self, timeObj, threshold):

		delta = self._delta(timeObj)

		#print(f"delta: {delta}")

		delta_minutes = delta.total_in_minutes()

		response = None

		if delta_minutes > threshold:
			response = "greater"

		elif delta_minutes < threshold:
			response = "less"

		else:
			response = "equal"

		return response

	def push_back(self, periodObj):

		self.disposable_h = self.hour
		self.disposable_m = self.minute

		self.disposable_h -= periodObj.hours
		self.disposable_m -= periodObj.minutes

		if self.disposable_h == 0:
			self.disposable_h = 24

		elif self.disposable_h < 0:			
			self.disposable_h = 24 - self.disposable_h

		if self.disposable_m == 60:
			self.disposable_m = 0

class Period:

	def __init__(self, hours, minutes, seconds=0):

		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds

	def __str__(self):

		return f"{self.hours}:{self.minutes}:{self.seconds}"

	def _tuple(self):
		return (self.hours, self.minutes, self.seconds)

	def total_in_minutes(self):
		return (self.hours * 60) + self.minutes

class Watcher:

	RESIZE_WIDTH = 20
	RESIZE_HEIGHT = 20
	LIGHT_THRESH = 50 # OF the 20x20 pixels how many must be bright it to trigger

	def __init__(self, capture):
		self.capture = capture

	def look(self):

		ret, frame = self.capture.read()

		dr = (Watcher.RESIZE_WIDTH, Watcher.RESIZE_HEIGHT)
		cv2.resize(frame, dr)

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		blurred = cv2.GaussianBlur(gray, (7,7), 0)
		T, blurred_gray_threshInv = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

		return ret, blurred_gray_threshInv

	def report(self, frame):

		count = 0 
		is_awake = False

		for r in range(len(frame)): # For every row
			for p in range(len(frame[r])): # For every pixel in that row


				r, g, b = frame[r][p]

				if r > 0 and g > 0 and b > 0:
					count += 1

		if count >= Watcher.LIGHT_THRESH:
			is_awake = True

		return is_awake

class SleepManager:

	TRESHOLD = 10
	rem_duration = Period(1, 30)

	def __init__(self, wake_up=Time(6, 30), duration=Period(6, 30)):

		self.target_wake = wake_up
		self.sleep_duration = duration

		self.wake_up = None

	def wake_up_time_update(self):

		response = "No Action"

		if self.wake_up == None:

			curr_time = Time(datetime.now().hour, datetime.now().minute)

			self.wake_up = curr_time.time_in(self.sleep_duration)

			if curr_time.hour > self.wake_up.hour:
				self.wake_up.day += 1

		comp = self.wake_up.compare(self.target_wake, SleepManager.TRESHOLD)

		if comp == "greater":

			self.wake_up.push_back(SleepManager.rem_duration)

		elif comp == "equal":
			response = "Wake up"

		return response