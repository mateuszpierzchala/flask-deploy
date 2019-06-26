#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 10:12:38 2019

@author: osboxes
"""

"""glowna aplikacja Flask"""

from flask import Flask

logging.basicConfig(level = logging.DEBUG, 
                    format='[%(asctime)s]:{} %(levelname)s% (message)s'.format(os.getpid()),
                    datefmt= '%Y-%m-%d %H:%M:%S',
                    handlers = logging.StreamHandler()])

logger = logging.getLogger()

def create_app():
    logger.info(f'Starting app in {config.APP_ENV} enviorment')
    app = Flask(__name__)
    app.config.from_object('config')
    api.init_app(app)
    #initialize SQLAlchemy
    db.init_app(app)
    #define hello world page
    
    @app.route('/')
    def hello_world():
        return 'hello world!'
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', debug = True) </td>
    </tr>
    <tr>
        <td>