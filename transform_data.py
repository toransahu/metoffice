#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:20:59 2017

@author: toran
"""
import  os
import pandas as pd
from lib import list_files

def fwf_to_csv(data_loc):
    """Convert all Fixed-Width data files to CSV."""
    
    colspec= [(1,9),
                (9,15),
                (15,23),
                (23,29),
                (29,37),
                (37,43),
                (43,51),
                (51,57),
                (57,65),
                (65,71),
                (71,79),
                (79,85),
                (85,93),
                (93,99),
                (99,107),
                (107,113),
                (113,121),
                (121,127),
                (127,135),
                (135,141),
                (141,149),
                (149,155),
                (155,163),
                (163,169),
                (169,177),
                (177,183),
                (183,191),
                (191,197),
                (197,205),
                (205,211),
                (211,219),
                (219,225),
                (225,233),
                (233,239)
                ]
    for txt_file in list_files(data_loc):
        csv_file = txt_file.replace('.txt', '.csv')
        if os.path.exists(csv_file):
            os.remove(csv_file)
        #df = pd.read_fwf(txt_file, 
        pd.read_fwf(txt_file, 
                         #names=cols, 
                         #widths= length,
                         colspecs = colspec,
                         #delim_whitespace = True,
                         #skipinitialspace = True,
                         #encoding = 'utf-8',
                         #skiprows = [0]
                         ).to_csv(csv_file)
    
