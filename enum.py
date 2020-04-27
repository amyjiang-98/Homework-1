#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 03:26:38 2020

@author: yushijiang
"""

from lxml import etree
import sys

input_file = sys.argv[1]

root = etree.parse(input_file).getroot()

theEle = root.getchildren()

result = {}

for element in theEle:
    for subelement in element.getchildren():
         if subelement.tag == 'TypeDescription':
             if subelement.text in result:
                    result[subelement.text] += 1
             else:
                 result[subelement.text] = 1
                 
print(sorted(result.items(), key=lambda x: x[1], reverse=True))