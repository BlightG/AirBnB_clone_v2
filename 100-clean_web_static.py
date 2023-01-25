#!/usr/bin/python3
'''cleans the archive files on remote servers using Fabric'''
import os
from fabric.api import env
from fabric.api import run
from fabric.api import local
env.hosts = ['100.26.20.157', '54.144.137.83']


def do_clean(number=0):
    ''' removes  n number of used archives '''
    count = 0  # used to count files statring with web_static
    entiries = run('ls /data/web_static/releases')
    files = entiries.split()
    web_files = []  # list of files stating with web_static

    for i in files:
        if i.startswith('web_static') is True:
            count += 1
            web_files.append(i)

    if len(web_files) == 0:
        return None

    web_files.sort()
    # print(web_files)
    if int(number) < 0:
        return None
    clean_count = count - int(number)
    # print('clean_count = {}'.format(clean_count))
    if clean_count > 0 and count > int(number) + 1:
        # if number == 0:
        #     run('rm /data/web_static/releases/{}'.format(web_files[0]))
        #     local('rm versions/{}.tgz'.format(web_files[0]))
        # else:
        for i in range(clean_count):
            print('/data/web_static/releases/{}'.format(web_files[i]))
            run('rm -r /data/web_static/releases/{}'.format(web_files[i]))
            local('rm versions/{}.tgz'.format(web_files[i]))
