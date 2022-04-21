import os
from pathlib import Path
from click.testing import CliRunner

from app import create_log_folder

runner = CliRunner()


def test_add():
    response = runner.invoke(create_log_folder)
    assert response.exit_code == 0
    file_name = Path(__file__)
    test_dir = file_name.parent
    proj_dir = test_dir.parent
    app_dir = proj_dir / "app"
    log_dir = app_dir / "logs"
    #root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    #logdir = os.path.join(root, '../logs')
    # make a directory if it doesn't exist
    assert log_dir.exists()
    #assert os.path.exists(log_dir) == True