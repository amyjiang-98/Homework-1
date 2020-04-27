#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:21:32 2020

@author: yushijiang
"""
from lxml import etree
import sys

input_file = sys.argv[1]
tree = etree.parse(input_file)

result = {}

for element in tree.getroot():
    theKey = element.find("Grade").text
    if not theKey:
        theKey = "NA"
    if theKey in result:
        result[theKey] = result[theKey] + 1
    else:
        result[theKey] = 1
        
for t in sorted(result):
    print(t, ":", result[t])
        
    