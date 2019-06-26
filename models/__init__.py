#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 10:06:41 2019

@author: osboxes
"""

"""definiuje klase User, ustawienia polaczenia z baza"""

import uuid

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User (db.Model):
    id = db.Column(db.String(), primary_key = True, default = lambda:str(uuid.uuid4()))
    username = db.Column(db.String())
    email = db.Column(db.String(), unique = True)