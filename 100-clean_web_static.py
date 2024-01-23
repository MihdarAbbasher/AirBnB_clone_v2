#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ['54.161.241.146', '18.210.14.165']


def do_clean(number=0):
    """Delete old archives.

    Args:
        number (int): The number of archives to keep.

    If number is 0 or 1, keeps only the most recent archive.
    """
    number = 1 if int(number) == 0 else int(number)

    sorted_archives = sorted(os.listdir("versions"))
    # remove archives form list of rm cmd
    [sorted_archives.pop() for i in range(number)]
    with lcd("versions"): # remove old archives
        [local("rm ./{}".format(arch)) for arch in sorted_archives]
    # rm in the remote server
    with cd("/data/web_static/releases"):
        # ls -t time sorted list -r recursively
        sorted_archives = run("ls -tr").split()
        sorted_archives = [a for a in sorted_archives if "web_static_" in a]
        [sorted_archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in sorted_archives]
