#!/usr/bin/env python

from json import dumps, loads
from os import walk
from sys import argv

dirpath = argv[1]
for (dirpath, dirnames, filenames) in walk(dirpath):
    for filename in filenames:
        if filename.endswith('.json'):
            with open('%s/%s' % (dirpath, filename), 'r+') as f:
                data = loads(f.read())
                data['editorJson'] = dumps(data['editorJson'])
                f.seek(0)
                f.write(dumps(data))
                f.truncate()