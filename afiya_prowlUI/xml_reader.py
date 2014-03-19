#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
try:
	import xml.etree.ElementTree as ET
except ImportError:
	print "Error importing module"
#Testing the function on "doc.xml"
def parse_xml(fname):
	val = {}
	tree = ET.parse(fname)
	root = tree.getroot()
	des = list(tree.iter())
	for child_elem in tree.iter():
		if child_elem is not root:
			val[child_elem.tag] = child_elem.text
	print val
	
fname = open("doc.xml")
parse_xml(fname)
	
