#!/usr/local/bin/python

import glob
import os
import json

class Tree:
    tree = {}

    def __init__(self, path, ext):
        self.path = path
        self.ext = ext

    def show(self):
        print(self.tree)

    def run(self):
        self.tree = self.scan(self.path)

    def get_list(self):
        return self.tree

    def scan(self, dir):
        os.chdir('/')
        os.chdir(dir)
        tree = {}
       # tree[dir] = {}
        counter = 0
        list = []
        for file in glob.glob('*'):
            if os.path.isdir(file):
                tree[file] = (self.scan(dir + '/' + file))
            elif file.endswith(self.ext):
                tree[counter] = file
            counter += 1
        return tree

print('This is a tree class collector - there is a diffrent collect type if You collect components or services')
user_input = ''
result = {'c': {}, 's': {}}
current_dir = os.getcwd()
while user_input != 'n':
    os.chdir(current_dir)
    path = input('enter pass to scan ')
    if not path.startswith('/'):
        path = os.getcwd()+'/'+path
        print('its not an absolute path - use current directory ('+path+')')
    fileType = ''
    while fileType not in ['c', 's']:
        fileType = input('enter c for component and s for service) ')

    if fileType == 'c':
        insertFileType = '.vue'
    else:
        insertFileType = '.js'

    inst = Tree(path, insertFileType)
    inst.run()
    result[fileType][path] = inst.get_list()
    user_input = input('add another path to scan? (y/n) ')

print(json.dumps(result))






