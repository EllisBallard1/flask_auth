from pathlib import Path
import os

import click
from flask.cli import with_appcontext
from app.db import db


@click.command(name='create-db')
@with_appcontext
def create_database():
    # get root directory of project
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root, '../../database')
    # make a directory if it doesn't exist
    if not os.path.exists(dbdir):
        os.mkdir(dbdir)
    db.create_all()


@click.command(name='create-log-folder')
@with_appcontext
def create_log_folder():
    # get root directory of project
    app_dir = Path(__file__).parent.parent
    # set the name of the apps log folder to logs
    logdir = app_dir / "logs"
    # make a directory if it doesn't exist
    if not logdir.exists():
        logdir.mkdir()
    # set name of the log file
    log_file = logdir / "info.log"
