# project/tests/test_config.py
import logging
import os

import app.config


def test_development_config(application):
    application.config.from_object('app.config.DevelopmentConfig')

    assert application.config['DEBUG']
    assert not application.config['TESTING']
<<<<<<< HEAD
    assert application.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:////home/myuser/database/db.sqlite'

=======
>>>>>>> a61b19e3141842f7d6f4660442d6ed40cd4e007d

def test_testing_config(application):
    application.config.from_object('app.config.TestingConfig')
    assert application.config['DEBUG']
    assert application.config['TESTING']
    assert not application.config['PRESERVE_CONTEXT_ON_EXCEPTION']
    assert application.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///:memory:'

def test_production_config(application):
    application.config.from_object('app.config.ProductionConfig')
    assert not application.config['DEBUG']
    assert not application.config['TESTING']
<<<<<<< HEAD
    assert application.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:////home/myuser/database/db.sqlite'
=======
>>>>>>> a61b19e3141842f7d6f4660442d6ed40cd4e007d
