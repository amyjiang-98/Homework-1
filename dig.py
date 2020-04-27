#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:26:48 2020

@author: yushijiang
"""

from lxml import html
from lxml import etree
import sys


def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    data = []
    parser = etree.HTMLParser()
    tree = etree.parse(input_file, parser)

    num_of_books = len(tree.xpath('//div[@class="AllEditionsItem-tile Recipe-default"]'))
    for i in range(num_of_books):
        book_title = tree.xpath('//*[@id="Content"]/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div['+str(i)+']/div[1]/div[1]/a/text()')
        book_author = tree.xpath('//*[@id="Content"]/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div['+str(i)+']/div[1]/div[2]/a/text()')
        book_format = tree.xpath('//*[@id="Content"]/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div['+str(i)+']/div[2]/div/div[2]/div[2]/div[1]/strong/text()')
        book_price = tree.xpath('//*[@id="Content"]/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div['+str(i)+']/div[2]/div/div[2]/div[1]/div[1]/div[2]/text()')
        book_condition = tree.xpath('//*[@id="Content"]/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div['+str(i)+']/div[2]/div/div[2]/div[2]/div[2]/strong/text()')
        book = [book_title, book_author, book_format, book_price, book_condition]
        data.append(book)
    
    def create_element(data, label):
        book = etree.Element("book")
        for i in range(len(data)):
            if data[i]:
                etree.SubElement(book, label[i]).text = data[i][0]
            else:
                etree.SubElement(book, label[i]).text = ""
        return book

    root = etree.Element("books")
    label = ["Title", "Author", "Format", "Price", "Condition"]
    for i in range(1, len(data)):
        sub_element = create_element(data[i], label)
        root.append(sub_element)
    
    etree.tostring(root, pretty_print=True)
    
    f = open(output_file, "wb")
    f.write(etree.tostring(root, pretty_print=True))
    f.close()

main()
