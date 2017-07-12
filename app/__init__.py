#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
author: ingbyr
website: www.ingbyr.com
"""
import configparser
import logging
import os

__author__ = 'InG_byr'

# Log settings

# logging.basicConfig(filename='GUI-YouGet.log',
#                     level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s >>> %(message)s',
#                     datefmt='%b%d %Y %H:%M:%S',
#                     filemode='w')

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s >>> %(message)s',
                    datefmt='%b%d %Y %H:%M:%S')

log = logging

# app config init
config = configparser.ConfigParser()
config.read("config.ini")
if not config.has_option("common", "out_put_dir"):
    config["common"]["out_put_dir"] = os.getcwd()
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
