#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:17:54 2019

@author: osboxes
"""

"""to zestaw klas konfiguracyjnych z ktorych jedna jest wybierana przez "APP_ENV" 
kiedy aplikacja zostanie uruchomiona kod w __init__.py utworzy instancje jednej z tych klas nadpisujac 
wartosci pol zmiennymi srodowiskowymi (jesli istnieja)"""

class BaseConfig():
    API_PREFIX = '/api'
    TESTING = False
    DEBUG = False
    
class Dev Config(BaseConfig)