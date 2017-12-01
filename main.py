#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 20:57:13 2017

@author: toran
"""
import platform
from download_data import download_data
from clean_data import clean_data
from transform_data import fwf_to_csv

regions = ['UK', 'England', 'Wales', 'Scotland']
attributes = ['Tmax', 'Tmin', 'Tmean', 'Sunshine', 'Rainfall']


## check in which pc i'm working
if platform.system() == 'Windows':
    # data_loc = "D:\Toran\WorkSpace\practice\interview\kisanhub\data"
    data_loc = ".\data"
    proxies = {
        "http": "http://toran.sahu:L440Qthink@10.74.91.103:80",
        "https": "http://toran.sahu:L440Qthink@10.74.91.103:80",
    }
else:
    # data_loc = "/mnt/ExternalHDD/E/workSpace/practice/interview/kisanhub/data"
    data_loc = "./data"
    proxies = {
        "http": None,
        "https": None,
    }

if __name__ == '__main__':
    print(download_data.__doc__)
    download_data(regions, attributes,data_loc,proxies)
    print(clean_data.__doc__)
    clean_data(data_loc)
    print(fwf_to_csv.__doc__)
    fwf_to_csv(data_loc)
    
