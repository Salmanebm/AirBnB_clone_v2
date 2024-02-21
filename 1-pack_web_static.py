#!/usr/bin/python3
""" This fabric script does the follwing stuff:
    - Creates versions folder if it doesn't exist
    - Creates .tgz file of all the web_static folder components """

from fabric.api import local
from datetime import datetime


def do_pack():
    """ creates an archive compressed file """
    local("mkdir -p versions")
    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "web_static_{}".format(time_now)
    local("tar -cvzf versions/{}.tgz web_static/*".format(filename))
