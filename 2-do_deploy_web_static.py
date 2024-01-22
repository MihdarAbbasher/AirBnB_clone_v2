#!/usr/bin/python3
""" deploy  from archive
"""
from fabric.api import *
from datetime import datetime
from os import path


env.user = 'ubuntu'
env.ssh_key_file = '/alx.school'
env.hosts = ['54.161.241.146', '18.210.14.165']


def do_deploy(archive_path):
    """deploy web files from the contents of archive"""

    try:
        if not (path.exists(archive_path)):
            return False


        put(archive_path, '/tmp/')
        f_path = '/data/web_static/releases/web_static_'
        f_name = archive_path[-18:-4]
        run('sudo mkdir -p {}{}/'.format(f_path, f_name))
        # uncompress archive
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
                    .format(f_name, f_name))
        run('sudo rm /tmp/web_static_{}.tgz'.format(f_name))
        # move contents into host web_static
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(f_name, f_name))
        # remove tmp web_static dir
        run('sudo rm -rf /data/web_static/releases/web_static_{}/\
                web_static'.format(f_name))

        # remove existing sym link & create new one
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s /data/web_static/releases/web_static_{}/\
 /data/web_static/current'.format(f_name))
    except:
        return False

    return True
