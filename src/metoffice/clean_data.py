# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 20:10:43 2017

@author: toran.sahu
"""

from metoffice.lib import list_files


def clean_data(data_loc):
    """Clean downloaded data."""

    files = list_files(data_loc)

    for file in files:
        # read file
        with open(file, 'r') as f:
            lines = f.readlines()

        # remove first 7 lines
        # write lines to the file
        with open(file, 'w') as f:
            lines = lines[7:]
            f.writelines(lines)
