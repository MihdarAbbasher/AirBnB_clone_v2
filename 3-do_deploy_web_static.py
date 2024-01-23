#!/usr/bin/python3
from fabric.api import local
from datetime import date
from time import strftime
from fabric.api import *
from datetime import datetime
from os import path

env.user = 'ubuntu'
env.key_filename = '/alx/school'
env.hosts = ['54.161.241.146', '18.210.14.165']

def do_pack():
    """Generate archive from the contents of web_static folder"""

    f_name = strftime("%Y%m%d%H%M%S")
    full_name = "versions/web_static_{}.tgz".format(f_name)
    try:
        local("mkdir -p versions")
        local("tar -czvf {} web_static/".format(full_name))

        return full_name

    except Exception as e:
        return None






def do_deploy(archive_path):
    """deploy web files from the contents of archive"""

    try:
        if not (path.exists(archive_path)):
            return False

        put(archive_path, '/tmp/')
        f_name = archive_path[:-4].rsplit('/', 1)[-1] or archive_path[:-4]
        f_path = '/data/web_static/releases/{}'.format(f_name)
        run('sudo mkdir -p {}/'.format(f_path))
        # uncompress archive
        run('sudo tar -xzf /tmp/{}.tgz -C {}/'.format(f_name, f_path))
        run('sudo mv {}/web_static/* {}/'.format(f_path, f_path)
        run("rm -rf /data/web_static/releases/{}/web_static".format(f_name))
        run('sudo rm /tmp/{}.tgz'.format(f_name))
        # remove existing sym link & create new one
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}/ /data/web_static/current'.format(f_path))
    except:
        return False
    return True

def deploy():
    """Create and distribute an archive to my web servers."""
    file_name = do_pack()
    if file_name is None:
        return False
    return do_deploy(file_name)
