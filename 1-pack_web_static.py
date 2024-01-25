#!/usr/bin/python3
from fabric.api import local
from datetime import date
from time import strftime


def do_pack():
    """Generate archive from the contents of web_static folder
    -c − This creates an archive file.
    -x − The option extracts the archive file.
    -f − Specifies the filename of the archive file.
    -v − This prints verbose information for any tar operation on the terminal.
    -t − This lists all the files inside an archive file.
    -u − This archives a file and then adds it to an existing archive file.
    -r − This updates a file or directory located inside a .tar file
    -z − Creates a tar file using gzip compression
    -j − Create an archive file using the bzip2 compression
    -W − The -w option verifies an archive file"""

    filename = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz -C web_static ."
              .format(filename))

        return "versions/web_static_{}.tgz".format(filename)

    except Exception as e:
        return None
