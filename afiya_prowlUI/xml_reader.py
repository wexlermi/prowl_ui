#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from collections import OrderedDict
#from elementtree.ElementTree import ElementTree
try:
 	import xml.etree.ElementTree as ET
except ImportError:
 	print ("Error importing module")
#Testing the function on "doc.xml"
def parse_xml(fname):
	val = OrderedDict()
	tree = ET.parse(fname)
	root = tree.getroot()
	des = list(tree.iter())
	for child_elem in tree.iter():
		if child_elem is not root:
			val[child_elem.tag] = child_elem.text
	return val

def modify_xml(fname):
	#print("hello")
	tree = ET.ElementTree(file=fname)
	root = tree.getroot()

	for child_elem in tree.iter():
		if child_elem is not root:
			print(child_elem.tag,child_elem.text)
			child_elem.text = "1"

	#for child_elem in tree.iter():
	#	print(child_elem.tag, child_elem.text)

	tree.write(sys.stdout, encoding="unicode")
			
	#tree.write(sys.stdout)


fname = 'doc.xml'
#f = open(fname, "w+")
#parse_xml(fname)
modify_xml(fname)
