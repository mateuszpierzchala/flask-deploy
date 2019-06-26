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
    
class DevConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_password@db-postgres:5432/flask-deploy'
    CELERY_BROKER = 'pymap://rabbit_user:rabit_password@borker-rabiitmq//'
    CELERY_RESULT_BACKEND = 'rpc://rabbit_user:rabiit_password@broker-rabiitmq//'
    
    
class ProductionConfig(BaseConfig):
    FLASK_ENV ='production'    
    SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_password@db-postgres:5432/flask-deploy'
    CELERY_BROKER = 'pymap://rabbit_user:rabit_password@borker-rabiitmq//'
    CELERY_RESULT_BACKEND = 'rpc://rabbit_user:rabiit_password@broker-rabiitmq//'
    
class TestConfig(BaseConfig):
    FLASK_ENV ='development'
    TESTING = True
    DEBUG = True
    #ustaw zeby celery zawsze wykonywal zadania synchronicznie w tymsamym procesie
    CELERY_ALWAYS_EAGER = True