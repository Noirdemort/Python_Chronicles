import os
import sys
import time

ALARM = raw_input()
Song = "/root/Music/NewDivide.mp3"

while True:
	os.system("clear")
	print("Alarm set at %s" % ALARM)
	start_time = time.strftime("%H:%M:%S")
	sys.stdout.write("Time : " + start_time)
	sys.stdout.flush()
	time.sleep(0.1)
	if start_time == ALARM:
		os.system("mplayer %s" % Song)
		break
