#!/usr/bin/python3
""" This fabric script does the follwing stuff:
    - distributes an archive to my web servers """

from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['ubuntu@54.174.144.6', 'ubuntu@34.229.137.175']
env.key_filename = ['~/.ssh/id_rsa']


def do_pack():
    """ creates an archive compressed file """
    local("mkdir -p versions")
    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "web_static_{}".format(time_now)
    local("tar -cvzf versions/{}.tgz web_static/*".format(filename))


def do_deploy(archive_path):
    """ distributes an archive to web servers """
    if not path.isfile(archive_path):
        return False

    remote_file = archive_path.split('/')[-1]
    remote_name = remote_file.split('.')[0]

    if put(archive_path, '/tmp/{}'.format(remote_file)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}"
           .format(remote_name)).failed is True:
        return False
    if run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
           .format(remote_file, remote_name)).failed is True:
        return False
    if run('rm -r /tmp/{}'.format(remote_file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/"
           .format(remote_name, remote_name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static"
           .format(remote_name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run('ln -sf /data/web_static/releases/{}/ /data/web_static/current'
           .format(remote_name)).failed is True:
        return False
    return True
