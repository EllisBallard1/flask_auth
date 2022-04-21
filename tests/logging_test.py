import logging
from logging import config
from pathlib import Path


def test_debug():
    file_name = Path(__file__)
    test_dir = file_name.parent
    proj_dir = test_dir.parent
    app_dir = proj_dir / "app"
    log_dir = app_dir / "logs"
    debug_file = log_dir / "errors.log"
    assert debug_file.exists()


def test_request():
    file_name = Path(__file__)
    test_dir = file_name.parent
    proj_dir = test_dir.parent
    app_dir = proj_dir / "app"
    log_dir = app_dir / "logs"
    request_file = log_dir / "request.log"
    assert request_file.exists()

