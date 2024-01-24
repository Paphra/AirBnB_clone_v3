#!/usr/bin/python3
"""deploy_web_static module
Packs the contents of the folder web_static into a .tgz file and distributes it
"""
from fabric.api import local, env, put, run, sudo
from datetime import datetime
import os

env.hosts = ['100.25.119.244', '54.89.107.222']


def do_pack():
    """"do_pack function
    Packs the contents of 'web_static' folder to a .tgz archive
    Returns:
        None: if there is a problem, otherwise, the location of the archive
    """
    if not hasattr(env, 'packed_archive'):
        try:
            local("mkdir -p versions")

            time_format = "%Y%m%d%H%M%S"
            archive_name = "web_static_{}.tgz".format(
                    datetime.utcnow().strftime(time_format))
            local("tar -cvzf versions/{} web_static".format(archive_name))
            archive_path = os.path.join("versions", archive_name)
            env.packed_archive = archive_path
            return archive_path
        except Exception as e:
            return None
    else:
        return env.packed_archive


def do_deploy(archive_path):
    """do_deploy function
    Deploys the archive to the servers
    Args:
        archive_path (str): the location of the archive
    Returns:
        bool: True if all goes well, otherwise, false
    """
    if not os.path.exists(archive_path):
        return False

    try:
        archive_filename = archive_path.split('/')[-1].split('.')[0]

        put(archive_path, '/tmp/')

        run("mkdir -p /data/web_static/releases/{}/".format(
                archive_filename))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            archive_filename + ".tgz", archive_filename))
        run("rm /tmp/{}".format(archive_filename + ".tgz"))
        run(("mv /data/web_static/releases/{}/web_static/*"
            " /data/web_static/releases/{}/").format(
                archive_filename, archive_filename))
        run("rm -rf /data/web_static/releases/{}/web_static".format(
            archive_filename))
        run("rm -rf /data/web_static/current")
        run(("ln -s /data/web_static/releases/{}/"
            " /data/web_static/current").format(archive_filename))
        print("New version deployed!")
        return True
    except Exception as e:
        return False


def deploy():
    """deploy function
    Call do_pack then do_deploy
    Returns:
        The return value of do_deploy, else False if no archive is created
    """
    path = do_pack()
    if path is None:
        return False

    return do_deploy(path)
