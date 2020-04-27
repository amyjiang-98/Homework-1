#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 22:34:29 2020

@author: yushijiang
"""
import sys
import cvs

input_file = sys.argv[1]
output_file = sys.argv[2]

csvFile = input_file
xmlFile = output_file

csvData = csv.reader(open(csvFile))

xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0"?>' + "\n")
# there must be only one top-level tag
xmlData.write('<FoodServices>' + "\n")

rowNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row
        # replace spaces w/ underscores in tag names
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
    else: 
        xmlData.write('<FoodService>' + "\n")
        for i in range(len(tags)):
            xmlData.write('    ' + '<' + tags[i] + '>' \
                          + row[i] + '</' + tags[i] + '>' + "\n")
        xmlData.write('</FoodService>' + "\n")
            
    rowNum +=1

xmlData.write('</FoodServices>' + "\n")
xmlData.close()