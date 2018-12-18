#!/usr/bin/python3

from sys import path
from os.path import realpath, dirname
path.append(dirname(realpath(__file__)))
import get_lang_list
import detect_lang
import translate