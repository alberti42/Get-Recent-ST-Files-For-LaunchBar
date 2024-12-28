#!/usr/bin/env -S -P/usr/local/bin:${PATH} python3
# coding: utf-8
#
# LaunchBar Action Script

import os.path
import json

DEBUG = False

def plist_path():
    return '~/Library/Application Support/Sublime Text/Local/recent_files_history.json'

def file_exist(item_path):
	return os.path.exists(item_path)
    
def print_file_size(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)
    
# def create_children_items(item_path):
#     item_path = item_path.encode(locale.getpreferredencoding())
#     children = []
#     children.append(dict(title = os.path.basename(item_path), label = "Name"))
#     children.append(dict(title = item_path, label = "Pfad"))
#     children.append(dict(title = datetime.fromtimestamp(os.path.getmtime(unicode(item_path,"utf-8"))).ctime(), label = "Erstellt", icon = "at.obdev.LaunchBar:CalendarEventDate"))
#     if os.path.isfile(item_path):
#         children.append(dict(title = print_file_size(os.path.getsize(unicode(item_path,"utf-8"))), label = "Größe", icon = "at.obdev.LaunchBar:InfoTemplate"))
#     return children
    
# def create_main_item_alt(item_path):
#     return dict(title = os.path.basename(item_path), subtitle = os.path.dirname(item_path),
#     path = item_path,
#     action = "open_with_sublime.py",
#     actionRunsInBackground = "true",
#     children = create_children_items(item_path),
#     icon = "com.sublimetext.4"
#     )

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
