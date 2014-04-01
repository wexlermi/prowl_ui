#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from collections import OrderedDict
from PyQt4 import QtGui, QtCore
# try:
#     import xml.etree.cElementTree as ET
# except ImportError:
#     import xml.etree.ElementTree as ET



from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement




xmlfile_name = ""

#Added the function to parse the XML and return (name,value) pairs


    #for child_elem in tree.iter():
    #   print(child_elem.tag, child_elem.text)

    #tree.write(sys.stdout)

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
        self.setWindowTitle('OWL Configurator')
        self.setWindowIcon(QtGui.QIcon('owl.ico'))
        self.show()
        
        
    def showDialog(self):
        global xmlfile_name
        xmlfile_name = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '~')
        data = self.parse_xml(xmlfile_name)
        self.text_boxes = {}
        for key,value in data.items():
            txt_box = QtGui.QLineEdit()
            txt_box.setText(str(value))
            self.xml_values_layout.addRow(key, txt_box)
            self.text_boxes[key] = txt_box
        

        self.reconfigure_xml_btn = QtGui.QPushButton('Save XML File')
        #self.save_xml_btn = QtGui.QPushButton('Save As')
        self.layout.addWidget  (self.reconfigure_xml_btn)
        #self.layout.addWidget(self.save_xml_btn)
        self.reconfigure_xml_btn.clicked.connect(self.modify_xml)

    def parse_xml(self, fname):
        val = OrderedDict()
        self.tree = ET.parse(fname)
        #root = tree.getroot()
        #des = list(tree.iter())
        for child_elem in self.tree.find('./e/default'):
            #if child_elem is not root:
            val[child_elem.tag] = child_elem.text
        return val

    def modify_xml(self):
        #print(self.xml_values_layout.)
        #tree = ET.ElementTree(file=xmlfile_name)
        #print(tree)
        #root = tree.getroot()

        for child_elem in self.tree.find('./e/default'):
            #if child_elem is not root:
            #print(child_elem.tag,child_elem.text)
            value = str(self.text_boxes[child_elem.tag].text())
            child_elem.text = value
            #child_elem.text = "1"

        self.tree.write(xmlfile_name, encoding="unicode")
            

        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = XmlEdit()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
