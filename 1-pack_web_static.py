#!/usr/bin/python3
'''script to generate tgz archive from the contents of web_static'''
from fabric.api import local
import os


def do_pack():
    '''a function to compress files'''
    if not os.path.isdir('versions'):
        local('mkdir versions')
    local('tar -cavf "web_static_$(date +"%Y%m%d%h%m%s").tar.gz" web_static')
    local('mv web_static_* versions')
