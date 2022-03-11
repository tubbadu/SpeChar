import sys, subprocess
from time import sleep

sleep(0.1)

def spawn_program_and_die(program, exit_code=0):
	subprocess.Popen(program)
	sys.exit(exit_code)


def xdotool(s):
	spawn_program_and_die(['xdotool', 'type', s])
	exit()

try:
	xdotool(str(sys.argv[1]))
except:
	print("error")
