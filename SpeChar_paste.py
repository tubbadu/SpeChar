from pyautogui import hotkey
import sys
from time import sleep
try:
	flag = sys.argv[1]
except:
	flag = "noflag"
sleep(0.1)
if flag == 'shift':
	hotkey('ctrl', 'shift', 'v')
elif flag == 'noflag' or flag == '':
	hotkey('ctrl', 'v')
else:
	print ("Unknown flag")
