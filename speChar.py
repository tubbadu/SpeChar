#!/usr/bin/python3
"""
	speChar by Tubbadu

	TODO:
	* change font
	* get screen size automatically
	* tidy up
	* change scrollbar to the native one (don't know why it's different)
"""
from operator import index
import sys, os, subprocess

#default values
PyQt_VERSION = 5
LANGUAGE = "en"
EMOJI = False

#reading arguments values
args = sys.argv[1:]
if "-l" in args:
	LANGUAGE = args[args.index("-l") + 1]

if "-v" in args:
	PyQt_VERSION = int(args[args.index("-v") + 1])

if "--emoji" in args:
	EMOJI = True

#global variables

path = os.path.abspath(os.path.dirname(__file__))
if EMOJI:
	configPath = path + "/emoji_" + LANGUAGE.strip() + ".config"
else:
	configPath = path + "/speChar_" + LANGUAGE.strip() + ".config"
iconPath = path + "/speCharIcon.ico"
screenSize = (None, None)

#check if language is supported
if not os.path.isfile(configPath):
	print(f"file {configPath} not found: Perhaps \"{LANGUAGE}\" language is not supported yet! Add it yourself in the github page (really easy!): https://github.com/tubbadu/SpeChar/pulls")
	exit()



if PyQt_VERSION == 5:
	from PyQt5.QtCore import Qt
	from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QListWidget, QListWidgetItem
	from PyQt5.QtGui import QFont, QIcon

	Key_Escape = Qt.Key_Escape
	Key_Enter = Qt.Key_Enter
	Key_Return = Qt.Key_Return
	Key_Down = Qt.Key_Down
	Key_Up = Qt.Key_Up

elif PyQt_VERSION == 6:
	from PyQt6.QtCore import Qt
	from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QListWidget, QListWidgetItem
	from PyQt6.QtGui import QFont, QIcon

	Key_Escape = Qt.Key.Key_Escape
	Key_Enter = Qt.Key.Key_Enter
	Key_Return = Qt.Key.Key_Return
	Key_Down = Qt.Key.Key_Down
	Key_Up = Qt.Key.Key_Up
else:
	print("Error: PyQt_VERSION not supported")
	exit(1)



def getConfig():
	specialCharacters = list()
	with open(configPath, 'r', encoding="utf16") as infile:
		for line in infile:
			add = line.strip().split('-')
			specialCharacters.append([add[0].strip(), add[1].strip()])
	return specialCharacters

def write(s):
	print(s)
	#subprocess.Popen(['xdotool', 'type', s])
	from pynput.keyboard import Controller
	import pyperclip
	keyboard = Controller()
	keyboard.type(s)
	pyperclip.copy(s)


def refreshList(txt):
	ret = []
	for element in specialCharacters:
		if txt.lower() in element[1].lower():
			ret.append(QListWidgetItem(element[0]))
	return ret

specialCharacters = getConfig()
lq = refreshList("")


class Main(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	
	def keyPressEvent(self, e):
		if e.key() == Key_Escape:
			self.close()
		elif e.key() == Key_Enter or e.key() == Key_Return:
			# print current selection (then closes app)
			self.close()
			write(self.lbox.currentItem().text())
			
		elif e.key() == Key_Down:
			try:
				self.lbox.setCurrentRow(self.lbox.currentRow() + 1)
			except Exception as e:
				print(e)
		elif e.key() == Key_Up:
			try:
				self.lbox.setCurrentRow(self.lbox.currentRow() - 1)
			except Exception as e:
				print(e)

	def initUI(self):
		def textchanged():
			lbox.clear()
			lq = refreshList(str(self.tbox.text()))
			for el in lq:
				lbox.addItem(el.text())
			#now select first element
			lbox.setCurrentRow(0)

		def itemclicked(item):
			self.close()
			write(item.text())

		self.lbox = QListWidget(self)
		lbox = self.lbox
		for el in lq:
			lbox.addItem(el)
		lbox.resize(lbox.sizeHint())
		self.lbox.setFont(QFont('Noto Color Emoji'))
		lbox.itemClicked.connect(itemclicked)
		self.tbox = QLineEdit(self)
		tbox = self.tbox
		tbox.textChanged.connect(textchanged)
		lbox.move(0, 0)
		lbox.setGeometry(5, 5, 100, 190)
		#tbox.move(115, 85)
		tbox.setGeometry(115, 83, 100, 25)
		tbox.setFocus()
		tbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
		lbox.setCurrentRow(0)		
		self.setGeometry(screenSize[0]//2 - 110, screenSize[1]//2 - 100, 220, 200)
		self.setWindowTitle('speChar')
		self.setWindowIcon(QIcon(iconPath))
		font = QFont()
		font.setPixelSize(15)
		self.setFont(font)
		self.show()


def main():
	app = QApplication(sys.argv)
	global screenSize
	screenSize = (app.primaryScreen().size().width(), app.primaryScreen().size().height())
	print(screenSize)
	ex = Main()
	sys.exit(app.exec())


if __name__ == '__main__':
	main()