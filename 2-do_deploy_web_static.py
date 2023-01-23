#!/usr/bin/python3
''' a script to distrbitue an arcive to the web servers listed'''
from fabric.api import run
from fabric.api import put
from fabric.api import env
import os
env.hosts = ['54.144.137.83', '100.25.165.152']
env.user = 'ubuntu'


def do_deploy(archive_path):
    ''' puts the archive file specified in archive_path
        to the desired weserver'''
#    env.hosts = ['54.144.137.83','100.25.165.152']
#    env.user = 'ubuntu'

#    if not isinstance(archive_path, str):
#        return False

    if os.path.exists(archive_path) is False:
        return False

    if put(archive_path, '/tmp').failed is True:
        return False

    run('mkdir -p /data/web_static/releses/{}'.format(archive_path.split('/')[0]))
    run('tar -xvf /tmp/{} --directory /data/web_static/releases/'.format(
        archive_path.split('/')[1]))
    run('rm /tmp/{}'.format(archive_path.split('/')[1]))
    run('rm /data/web_static/current')
    run('ln -s /data/web_static/releases/{} /data/web_static/current'
        .format(archive_path.replace('.tgz', '')))
    return True
