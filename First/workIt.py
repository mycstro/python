#!/usr/bin/python
# -*- coding: utf-8 -*-

import locale
import os
import re
import sys

# Replaced to /opt/....
path_to_share=""

# wait computer internet connection
os.system("sleep 10")

try:  # try python 3 import
    from urllib.request import urlopen
    from urllib.request import urlretrieve
    from configparser import ConfigParser
except ImportError:  # fall back to python2
    from urllib import urlretrieve
    # from urllib2 import urlopen
    # from ConfigParser import ConfigParser

# import xml.etree.ElementTree as ET

import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Notify', '0.7')
# from gi.repository import Gio
# from gi.repository import Gtk
from gi.repository import DynamicImporter as Notify
from subprocess import check_output

config_file_skeleton ="""[market]
# If you want to override the current Bing market dectection,
# set your preferred market here. For a list of markets, see
# https://msdn.microsoft.com/en-us/library/dd251064.aspx
area =
[directory]
# Download directory path. By default images are saved to
# /home/[user]/[Pictures]/BingWallpapers/
dir_path =
# Limit the size of the downloaded image directory
# Size should be specified in bytes. The minimum 
# limit is the size of 1 image (whatever size that image is)
# Set to negative value for unlimit. Default value is 100MiB
dir_max_size = 
"""

def get_config_file():
    """
    Get the path to the program's config file.

    :return: Path to the program's config file.
    """
    config_dir = os.path.join(os.path.expanduser('~'), '.config',
                              'test')
    init_dir(config_dir)
    config_path = os.path.join(config_dir, 'config.ini')
    if not os.path.isfile(config_path):
        with open(config_path, 'w') as config_file:
            config_file.write(config_file_skeleton)
    return config_path

def get_download_path():
    # By default images are saved to '/home/[user]/[Pictures]/BingWallpapers/'
    default_path = check_output("xdg-user-dir PICTURES", shell=True).strip().decode("utf-8") + "/Test"

    try:
        config = ConfigParser()
        config.read(get_config_file())
        path = config.get('directory', 'dir_path')

        return path or default_path
    except Exception:
        return default_path

def get_directory_limit():
    """
    Get the directory sized limit
    """
    config = ConfigParser()
    config.read(get_config_file())
    try:
        size = config.getint('directory', 'dir_max_size')
        return size
    except Exception:
        return 100 * 1024 * 1024

def init_dir(path):
    """
    Create directory if it doesn't exist.

    :param path: Path to a directory.
    """
    if not os.path.exists(path):
        os.makedirs(path)


def p3_dirscan(path):
    files = list()
    size = 0

    for e in os.scandir(path):
        entry = path + "/" + e
        if os.path.isfile(entry) and os.path.splitext(entry)[1] == ".jpg":
            s = os.path.getsize(entry)
            files.append(entry, s)
            size = size + s
    files = sorted(files)
    return files, size

def p2_dirscan(path):
    files = list()
    size = 0

    for e in os.listdir(path):
        entry = path + "/" + e
        if os.path.isfile(entry) and os.path.splitext(entry)[1] == ".jpg":
            s = os.path.getsize(entry)
            files.append((entry, s))
            size = size + s
    files = sorted(files)
    return files, size


def check_limit():
    download_path = get_download_path()
    (files, size) = p2_dirscan(download_path)
    max_size = get_directory_limit()
    while (max_size > 0 and size > max_size and len(files) > 1):
        os.remove(files[0][0])
        size = size - files[0][1]
        del files[0]


# def main():
#     """
#     Main application entry point.
#     """
#     app_name = 'WorkIt'
#     # Notify.init(app_name)
#     exit_status = 0
#
#     try:
#         # image_metadata = get_image_metadata()
#         # image_name = image_metadata.find("startdate").text + ".jpg"
#         # image_url = get_image_url(image_metadata)
#
#         download_path = get_download_path()
#         init_dir(download_path)
#         image_path = os.path.join(download_path)
#         # image_path = os.path.join(download_path, image_name)
#
#         if not os.path.isfile(image_path):
#             urlretrieve(image_path)
#             try:
#             # change_background_gnome(image_path)
#             except:
#             # change_background_cinnamon(image_path)
#             # change_screensaver(image_path)
#             # summary = 'Bing Wallpaper updated successfully'
#             # body = image_metadata.find("copyright").text.encode('utf-8')
#
#             text = str(image_name) + " -- " + str(body) + "\n"
#             # text = str(image_name) + " -- " + str(body) + "\n"
#             with open(download_path + "/image-details.txt", "a+") as myfile:
#                 myfile.write(text)
#
#         elif os.path.samefile(get_current_background_uri(), image_path):
#             summary = 'Unchanged'
#             body = ('%s already exists in directory' %
#                     image_metadata.find("copyright").text.encode('utf-8'))
#
#         else:
#             try:
#                 change_background_gnome(image_path)
#             except:
#                 change_background_cinnamon(image_path)
#             change_screensaver(image_path)
#             summary = 'Changed'
#             body = ('%s already exists in directory' %
#                     image_metadata.find("copyright").text.encode('utf-8'))
#         check_limit()
#
#     except Exception as err:
#         summary = 'Error executing %s' % app_name
#         body = err
#         print(body)
#         exit_status = 1
#
#     os.chdir(path_to_share)
#     icon = os.path.abspath("icon.svg")
#     app_notification = Notify.Notification.new(summary, str(body), icon)
#     app_notification.show()
#     sys.exit(exit_status)


if __name__ == '__main__':
    # main()
