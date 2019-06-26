#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:50:35 2019

@author: osboxes
"""

""" start i inicjalizacja workera celery ktory bedzie dzialal 
w osobnym kontenerze, inicjalizuje tez kontekst aplikacji flaask  
aby miec dostep do tego samego srodowiska co aplikacja """


from app import create_app

app=create_app()
app.app_context().push()

from tasks import celery