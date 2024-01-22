#!/usr/bin/python3
"""1-pack_web_static module
Packs the contents of the folder web_static into a .tgz file
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """"do_pack function
    Packs the contents of 'web_static' folder to a .tgz archive
    """
    try:
        local("mkdir -p versions")

        time_format = "%Y%m%d%H%M%S"
        archive_name = "web_static_{}.tgz".format(
                datetime.utcnow().strftime(time_format))
        local("tar -cvzf versions/{} web_static".format(archive_name))
        return os.path.join("versions", archive_name)
    except Exception as e:
        return None
