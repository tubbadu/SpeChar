#!/usr/bin/python3
"""
	SpeChar by Tubbadu

	TODO:
	* change font
	* get screen size automatically
	* tidy up
	* change scrollbar to native
"""
import sys, os, subprocess
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QListWidget, QListWidgetItem
from PyQt6.QtGui import QFont, QIcon# import setIcon

path = os.path.abspath(os.path.dirname(__file__))
pastePath = path + "/xdotool.py"
configPath = path + "/SpeChar.config"
screenSize = (1920, 1080) #TODO get automatically
specialCharacters = list()


def getConfig():
	global specialCharacters #, l_info #farla modificare con un return magari
	with open(configPath, 'r') as infile:
		for line in infile:
			add = line.strip().split('-')
			specialCharacters.append([add[0].strip(), add[1].strip()])

def write(s):
	print(s)
	subprocess.Popen(['xdotool', 'type', s])

def refreshList(txt):
	ret = []
	for element in specialCharacters:
		if txt.lower() in element[1].lower():
			ret.append(QListWidgetItem(element[0]))
	return ret
getConfig()
lq = refreshList("")




class Main(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()
	
	def keyPressEvent(self, e):
		#print(e.key())
		if e.key() == Qt.Key.Key_Escape.value:
			self.close()
		elif e.key() == Qt.Key.Key_Enter.value or e.key() == Qt.Key.Key_Return.value:
			# print current selection (then closes app)
			self.close()
			write(self.lbox.currentItem().text())
			
		elif e.key() == Qt.Key.Key_Down.value:
			try:
				self.lbox.setCurrentRow(self.lbox.currentRow() + 1)
			except Exception as e:
				print(e)
		elif e.key() == Qt.Key.Key_Up.value:
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
			print(item.text())

		
		self.lbox = QListWidget(self)
		lbox = self.lbox
		for el in lq:
			lbox.addItem(el)
		lbox.resize(lbox.sizeHint())
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

		'''layout = QVBoxLayout()

		layout.addWidget(lbox)
		layout.addWidget(tbox)

		widget = QWidget()
		widget.setLayout(layout)'''
		#self.setCentralWidget(widget)
		
		self.setGeometry(screenSize[0]//2 - 110, screenSize[1]//2 - 100, 220, 200)
		self.setWindowTitle('speChar')
		self.setWindowIcon(QIcon("/home/tubbadu/code/GitHub/SpeChar/SpeCharIcon.ico"))
		print(dir(self))
		font = QFont()
		font.setPixelSize(15)
		self.setFont(font)
		self.show()


def main():

	app = QApplication(sys.argv)
	ex = Main()
	sys.exit(app.exec())


if __name__ == '__main__':
	main()