#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

#Afiya: currently returning hard-coded values. please write this function to parse the xml file and return a similar sort of structure
def parse_xml(filename):
    return [('a', 1), ('b', 2), ('c', 3)]

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
        data = parse_xml(fname)
        for (name, value) in data:
            txt_box = QtGui.QLineEdit()
            txt_box.setText(str(value))
            self.xml_values_layout.addRow(name, txt_box)
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = XmlEdit()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
