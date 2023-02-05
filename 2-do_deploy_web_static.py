#!/usr/bin/python3
''' a script to distrbitue an arcive to the web servers listed'''
from fabric.api import run
from fabric.api import put
from fabric.api import env
import os
env.hosts = ["100.26.20.157", "54.144.137.83"]
env.user = 'ubuntu'


def do_deploy(archive_path):
    ''' puts the archive file specified in archive_path
        to the desired weserver'''

    if os.path.exists(archive_path) is False:
        return False

    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, '/tmp/{}'.format(file)).failed is True:
        return False

    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False

    if run('mkdir -p /data/web_static/releases/{}/'.
            format(name)).failed is True:
        return False

    if run('tar -xvf /tmp/{} -C /data/web_static/releases/{}/'.format(
           file, name)).failed is True:
        return False

    if run('rm /tmp/{}'.format(file)).failed is True:
        return False

    if run('mv /data/web_static/releases/{}/web_static/* '
           '/data/web_static/releases/{}/'.format(name, name)).failed is True:
        return False

    if run('rm -rf /data/web_static/current').failed is True:
        return False

    if run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.
           format(name)):
        return False

    return True
