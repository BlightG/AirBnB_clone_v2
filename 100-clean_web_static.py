#!/usr/bin/python3
'''cleans the archive files on remote servers using Fabric'''
import os
from fabric.api import env
from fabric.api import run
from fabric.api import local
env.hosts = ['100.26.20.157', '54.144.137.83']


def do_clean(number=0):
    ''' removes  n number of used archives '''
    # count = 0  # used to count files statring with web_static
    entiries = run('ls /data/web_static/releases')  # returns str
    local_entiries = os.listdir('versions')  # returns list
    files = entiries.split()
    local_files = []  # list of local files starting with web_static
    for i in range(len(local_entiries)):
        if local_entiries[i].startswith('web_static') is True:
            local_files.append(local_entiries[i])

    web_files = []  # list of files stating with web_static
    for i in files:
        if i.startswith('web_static') is True:
            # count += 1
            web_files.append(i)

    if len(web_files) == 0 or len(local_files) == 0:
        return None

    web_files.sort()
    local_files.sort()
    # print(web_files)
    # print(local_files)
    if int(number) < 0:
        return None
    clean_count = len(web_files) - int(number)
    # print('clean_count = {}'.format(clean_count))
    if clean_count > 1: 
        # if number == 0:
        #     run('rm /data/web_static/releases/{}'.format(web_files[0]))
        #     local('rm versions/{}.tgz'.format(web_files[0]))
        # else:
        for i in range(clean_count):
            # print('/data/web_static/releases/{}'.format(web_files[i]))
            run('rm -r /data/web_static/releases/{}'.format(web_files[i]))

    local_count = len(local_files) - int(number)
    if local_count > 1: 
        for i in range(local_count):
            local('rm versions/{}'.format(local_files[i]))
