#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
try:
	import xml.etree.ElementTree as ET
except ImportError:
	print "Error importing module"


#Added the function to parse the XML and return (name,value) pairs
def parse_xml(fname):
	val = {}
	tree = ET.parse(fname)
	root = tree.getroot()
	des = list(tree.iter())
	for child_elem in tree.iter():
		if child_elem is not root:
			val[child_elem.tag] = child_elem.text
	return val

class XmlEdit(QtGui.QWidget):
    
    def __init__(self):
        super(XmlEdit, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.layout = QtGui.QVBoxLayout()
        self.choose_xml_btn = QtGui.QPushButton('Select XML file')
        self.choose_xml_btn.clicked.connect(self.showDialog)
        self.xml_values = QtGui.QScrollArea()
        self.xml_values_layout = QtGui.QFormLayout()
        self.xml_values.setLayout(self.xml_values_layout)
        self.layout.addWidget(self.choose_xml_btn)
        self.layout.addWidget(self.xml_values)      
        self.setLayout(self.layout)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Edit Prowl XML file')
        self.show()
        
        
    def showDialog(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '~')
        data = {}
        data = parse_xml(fname)
        print data
        for key,value in data.items():
            txt_box = QtGui.QLineEdit()
            txt_box.setText(str(value))
            self.xml_values_layout.addRow(key, txt_box)
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = XmlEdit()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
