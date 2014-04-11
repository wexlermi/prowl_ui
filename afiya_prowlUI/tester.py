import sys
from collections import OrderedDict
from PyQt4 import QtGui, QtCore
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
import os

xmlfile_name = ""

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
        self.xmlfile_name = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '~')
        self.filename_alone = os.path.split(self.xmlfile_name)[1]
        self.xml_path_thing = './' + self.filename_alone + '/default'
        print(self.xml_path_thing)
        data = self.parse_xml(self.xmlfile_name)
        self.text_boxes = {}
        for key,value in data.items():
            txt_box = QtGui.QLineEdit()
            txt_box.setText(str(value))
            self.xml_values_layout.addRow(key, txt_box)
            self.text_boxes[key] = txt_box
        
        self.reconfigure_xml_btn = QtGui.QPushButton('Save XML File')
        self.layout.addWidget  (self.reconfigure_xml_btn)
        self.reconfigure_xml_btn.clicked.connect(self.modify_xml)

    def parse_xml(self, fname):
        val = OrderedDict()
        self.tree = ET.parse(fname)
        for child_elem in self.tree.find(self.xml_path_thing):
            val[child_elem.tag] = child_elem.text
            print (child_elem.tag , child_elem.text)
        return val


    def modify_xml(self):
        for child_elem in self.tree.find(self.xml_path_thing):
            value = str(self.text_boxes[child_elem.tag].text())
            child_elem.text = value
        self.tree.write(self.xmlfile_name, encoding="unicode")
            
def main():
    app = QtGui.QApplication(sys.argv)
    ex = XmlEdit()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()