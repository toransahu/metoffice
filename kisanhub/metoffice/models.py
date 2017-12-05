#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 22:15:49 2017

@author: toran
"""

from django.db import models
from adaptor.model import CsvDbModel


class Weather(models.Model):
    region = models.CharField(max_length=15)
    attribute = models.CharField(max_length=15)
    season = models.CharField(max_length=4)
    year = models.IntegerField(default=9999)
    value = models.FloatField(default=999999)

    class Meta:
        indexes = [
            models.Index(fields=['region', 'year', 'season', 'attribute']),
        ]
        unique_together = (("region", "year", "season", "attribute"), )

    def __str__(self):
        return self.region, self.season, self.year, self.attribute, self.value


class Climate(models.Model):
    region = models.CharField(max_length=15)
    season = models.CharField(max_length=4)
    year = models.IntegerField(default=0)
    tmin = models.FloatField(default=0)
    tmean = models.FloatField(default=0)
    tmax = models.FloatField(default=0)
    sunshine = models.FloatField(default=0)
    rainfall = models.FloatField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['region', 'year', 'season']),
        ]
        unique_together = (("region", "year", "season"), )

    def __str__(self):
        return self.region, self.season, self.year, self.tmin, self.tmean, self.tmax


class WeatherCsvModel(CsvDbModel):
    class Meta:
        dbModel = Weather
        delimiter = ","
        has_header = True
