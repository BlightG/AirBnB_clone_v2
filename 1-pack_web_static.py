#!/usr/bin/python3
'''script to generate tgz archive from the contents of web_static'''
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    '''a function to compress files'''
    if not os.path.isdir('versions'):
        if local('mkdir -p versions').failed is True:
            return None
    dt = datetime.utcnow()
    file = "versions/web_static_{:04d}{:02d}{:02d}{:02d}{:02d}{:02d}.tgz"\
           .format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    if local('tar -cavf {} web_static'.format(file)).failed is True:
        return None

    return file
