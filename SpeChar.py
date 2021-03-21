#!/usr/bin/python3

import PySimpleGUI as sg
import pyperclip
import os
import subprocess
import sys
import pyautogui
sg.theme('DarkTeal12')
pastePath = "/home/tubbadu/code/GitHub/SpeChar/SpeChar_paste.py" 
configPath = "/home/tubbadu/code/GitHub/SpeChar/SpeChar.config"
screenSize = (1920, 1080)

def spawn_program_and_die(program, exit_code=0): #copiata lol
    """
    Start an external program and exit the script 
    with the specified return code.

    Takes the parameter program, which is a list 
    that corresponds to the argv of your command.
    """
    # Start the external program
    subprocess.Popen(program)
    # We have started the program, and can suspend this interpreter
    sys.exit(exit_code)

specialCharacters, justChar = [], []

def refreshList(txt):
	ret = []
	for element in specialCharacters:
		if txt.lower() in element[1].lower():
			ret.append(element[0])
	return ret

def paste(ch, shift=False):
	if(shift):
		flag = 'shift'
	else:
		flag = ''
	pyperclip.copy(ch)
	spawn_program_and_die(['python3', pastePath, flag])
	exit()

def main():
	try:
		global justChar
		with open(configPath, 'r') as infile:
			
			for line in infile:
				add = line.strip().split('-')
				specialCharacters.append([add[0].strip(), add[1].strip()])
				justChar.append(add[0].strip())
		justChar[0] = justChar[0] + ' <'

		currentMouseX, _ = pyautogui.position()
		pos = ((screenSize[0] - 300)/2, (screenSize[1] - 185)/2)
		if currentMouseX > screenSize[0]:
			#sono nel secondo schermo
			pos = (pos[0] + screenSize[0], pos[1])

		layout = [[sg.Listbox(values=justChar, size=(3, 6), key='--listbox--', enable_events=True, font=("DejaVu Math TeX Gyre", 15)), sg.Column([[sg.Checkbox("shift", default=False, key='--checkbox--', enable_events=True)], [sg.Input(key='--search--', font=("Helvetica", 15), size=(12, None))]], justification='right')]]
		window = sg.Window('SpeChar', layout, element_justification='center', return_keyboard_events=True, size=(234, 150), location=pos, icon='/home/tubbadu/code/GitHub/SpeChar/SpeCharIcon.ico')
		index = 0
		oldlen = len(justChar)
		while(True):
			event, values = window.read()
			shift = values['--checkbox--']
			if 'Shift' in event:
				window['--checkbox--'].update(value = not shift)
			if 'Up' in event and index > 0:
				index -= 1
			elif 'Down' in event and index < len(justChar) - 1:
				index += 1
			
			txt = values['--search--']
			justChar = refreshList(txt)
			
			if oldlen != len(justChar):
				index = 0
			oldlen = len(justChar)

			if len(justChar) > 0: justChar[index] = justChar[index] + ' <'

			if 'KP_Enter' in event or 'Return' in event:
				# TODO aggiungere l'ordinamento maiuscola/minuscola, mettere la possibilità di navigare con le frecce
				ch = justChar[index].strip().strip('<').strip() #refreshList(txt)[0]
				paste(ch, shift)
			elif event == sg.WINDOW_CLOSED or 'Escape' in event:
				break
			elif event == '--listbox--':
				# è stato premuto un char!
				ch = values['--listbox--'][0]
				paste(ch, shift)

			if 'MouseWheel' not in event:
				window['--listbox--'].update(values = justChar)
			
			print(event)
		window.close()
	except Exception as e:
		print('An error occourred while running SpeChar:', e)
main()
