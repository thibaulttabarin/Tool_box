#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 11:45:25 2022

@author: thibault
"""
  
import pandas as pd
import sys

def main(csvFile, output="table_markdown.txt"):
    
    df = pd.read_csv(csvFile, engine='python')
    with open(output, 'w') as md:
        df.fillna('', inplace=True)
        df.to_markdown(buf=md, index=False)

def show_usage():
    
    print ("Usage : cvs_to_markdown.py <csv_file.csv> <table_markdown.txt>")


if __name__ == '__main__':

    if len(sys.argv) != 3:
         show_usage()
         sys.exit(1)
    else:
        csvFile = sys.argv[1]
        output = sys.argv[2]    
        main(csvFile, output=output)
 
             