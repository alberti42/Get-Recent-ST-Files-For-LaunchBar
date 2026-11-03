#!/usr/bin/env -S -P/usr/local/bin:${PATH} python3
# coding: utf-8
#
# LaunchBar Action Script

import os.path
import json

DEBUG = False

def plist_path():
    return '~/Library/Application Support/Sublime Text/Local/recent_files_history.json'

HOME = os.path.expanduser('~')

def file_exist(item_path):
    if not item_path.startswith(HOME):
        return False
    return os.path.exists(item_path)
    
def create_main_item(item_path):
    return dict(title = os.path.basename(item_path), subtitle = os.path.dirname(item_path),path = item_path)

try:
    with open(os.path.expanduser(plist_path())) as json_data:
        file_history = [d['file_name'] for d in json.load(json_data)]
        items = [create_main_item(item_path) for item_path in filter(file_exist,file_history)]
except Exception as e:
    if DEBUG:
        with open(os.path.expanduser('~/sublime_recent_file_error.log'),'w') as f:
            import traceback
            print(e.__str__().strip('\n'))
            print("{:s} - Traceback (most recent call last):\n".format(type(e).__name__) + \
                   "".join(traceback.format_tb(e.__traceback__)))
    items = []

print(json.dumps(items))
