#!/usr/bin/env python3
# coding: utf-8
#
# LaunchBar Action Script

import sys
import os.path
import json
import locale

if len(sys.argv) == 2:
    item = json.loads(sys.argv[1])
    os.system("open -b com.sublimetext.4 \"{}\"".format(item["path"].encode(locale.getpreferredencoding())))
