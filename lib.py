#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:02:18 2017

@author: toran
"""
import os
from os import listdir
from os.path import join, isfile

def list_files(data_loc):
    """Get downloaded data files."""
    
    files = [join(data_loc, f) for f in os.listdir(data_loc) if isfile(join(data_loc, f))]
    return files
