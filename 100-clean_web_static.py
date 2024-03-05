#!/usr/bin/python3
""" This script cleans unneccessary archive files """

from datetime import datetime
from fabric.api import *


def do_clean(number=0):
    """ Cleanes unneccessary archive files """
    archives = local("ls versions/", capture=True)
    archives_list = archives.splitlines()

    archives_date = []
    for file in archives_list:
        file_date = file.split(file.split('_')[-1].split('.')[0])
        file_date_conv = datetime.strptime(file_date, "%Y%m%d%H%M%S")
        archives_date.append(file_date_conv)

    archives_date = reversed(sorted(archives_date))

    if number in (0, 1):
