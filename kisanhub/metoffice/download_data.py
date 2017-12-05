# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 19:49:20 2017

@author: toran.sahu
"""
import os


def download_file(url, proxies):
    """Download a file from url as raw"""
    import requests

    res = requests.get(url, stream=True, proxies=proxies)
    return res


def save_file(loc, filename, response):
    """Save a raw file into disk"""
    import codecs

    file = os.path.join(loc, filename)
    with codecs.open(file, 'w', response.encoding) as f:
        f.write(response.text)


def download_data(regions, attributes, data_loc, proxies):
    """Download all data."""
    import shutil

    url_prefix = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets"

    # check existance of data folder
    if os.path.exists(data_loc):
        shutil.rmtree(data_loc, ignore_errors=True)
        os.makedirs(data_loc)
    else:
        os.makedirs(data_loc)

    ## download and save all the files
    for region in regions:
        for attribute in attributes:
            url = url_prefix + '/' + attribute + '/' + 'ranked' + '/' + region + '.txt'
            filename = attribute + '_' + region + '.txt'
            # download file
            response = download_file(url, proxies)
            # save file @ ./data/
            save_file(data_loc, filename, response)
