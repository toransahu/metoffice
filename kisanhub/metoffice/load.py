#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:48:12 2017

@author: toran
"""

from metoffice.models import Climate, Weather
from os.path import join
import csv
from os.path import basename
from metoffice.lib import list_files
import os

#=========================Not Using this approach==============================
def delete_all():
    Weather.objects.all().delete()


def csv_to_weather(data_loc):
    """Save data from CSV to DB"""

    # clean the table
    delete_all()

    # load fresh
    file = join(data_loc, 'consolidated.csv')
    with open(file) as c:
        # header = c.readline()
        c.readline()
        # cols = header.split(',')
        reader = list(csv.reader(c, delimiter=','))
        for row in reader:
            w = Weather(
                region=row[0],
                season=row[1],
                year=row[2],
                attribute=row[3],
                value=row[4])
            try:
                w.save()
            except:
                print("Problem while loading the row", row)

#==============================================================================



def create_or_update(aregion, aseason, ayear, attribute, val):
    """Create or Update record in DB"""
    

    # check for the unique row (region,season,year)
    record = Climate.objects.filter(region=aregion, season=aseason, year=ayear)

    if record.exists():
        # update
        if attribute == 'Tmax':
            record.update(tmax=val)
        elif attribute == 'Tmean':
            record.update(tmean=val)
        elif attribute == 'Tmin':
            record.update(tmin=val)
        elif attribute == 'Sunshine':
            record.update(sunshine=val)
        elif attribute == 'Rainfall':
            record.update(rainfall=val)
    else:
        # create
        if attribute == 'Tmax':
            c = Climate(region=aregion, season=aseason, year=ayear, tmax=val)
        elif attribute == 'Tmean':
            c = Climate(region=aregion, season=aseason, year=ayear, tmean=val)
        elif attribute == 'Tmin':
            c = Climate(region=aregion, season=aseason, year=ayear, tmin=val)
        elif attribute == 'Sunshine':
            c = Climate(
                region=aregion, season=aseason, year=ayear, sunshine=val)
        elif attribute == 'Rainfall':
            c = Climate(
                region=aregion, season=aseason, year=ayear, rainfall=val)
        c.save()
        return



def csv_to_climate(data_loc):
    """Save data from CSV to DB"""
    
    # delete old records
    Climate.objects.all().delete()
    
    files = [file for file in list_files(data_loc) if file.endswith('.csv')]
    cons_csv = os.path.join(data_loc,'consolidated.csv')
    if cons_csv in files:
        files.remove(cons_csv)

    for file in files:
        attribute, region = (os.path.splitext(basename(file))[0]).split('_')

        with open(file) as c:
            header = c.readline()
            cols = header.split(',')
            reader = list(csv.reader(c, delimiter=','))
            for i in range(1, len(cols) - 1, 2):
                season = cols[i]
                for row in reader:
                    val = row[i].strip()
                    year = row[i + 1].strip()
                    if val != '':
                        val = float(val)
                    else:
                        val = 9999999
                    if year != '':
                        #year = int(row[i+1].rstrip('.0'))
                        year = int(float(year))
                    else:
                        year = 9999
                    create_or_update(region, season, year, attribute, val)
                    #print(region,season,year, attribute, val)
