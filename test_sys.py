import cv2
from specialAlarm import Watcher, SleepManager, ring_alarm, sleep_survey
from datetime import datetime

def main():

	capture = cv2.VideoCapture(0)

	sleep_time = 5

	alarm = SleepManager()
	watcher = Watcher(capture)

	if capture.isOpened():
		while True:

			ret, frame = watcher.look() # look 
			is_awake = watcher.report(frame) # Report
	
			response = None

			if is_awake is False:
				response = alarm.wake_up_time_update()

			else: # In case of waking up after a period of trying to fall asleep
				alarm.target_wake = None

			if response == "Wake up":
				print(datetime.now())
				break

			time.sleep(sleep_time)

	else:
		print("Error, Camera not found")

def test_main():

	alarm = SleepManager()
	
	while True:

		is_awake = True

		response = alarm.wake_up_time_update()

		print(f"Wakeup?: {response}")


#if __name__ == "__main__":
main()