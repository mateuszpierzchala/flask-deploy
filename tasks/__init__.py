#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:17:54 2019

@author: osboxes
""" 
"""inicjalizacja polaczenia z celery"""

from celery import Celery
import config

def make_celery():
    celery=Celery(__name__, broker=config.CELERY_BROKER)
    celery.conf.update(config.as_dict())
    return celery

celery = make_celery()