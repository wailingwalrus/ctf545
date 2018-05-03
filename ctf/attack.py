#!/usr/bin/python

import os
import sys
import re

class Vulnerability():
    def __init__(path, lineno, line):
        self.path = path
        self.lineno = lineno
        self.line = line
        
def analyze(path,srcfile, search_printf):
    lines = srcfile.readlines()
    cnt = 1
    for line in lines:
        regex = "(exec|system|strcpy|argv|gets|read|strncpy|popen|printf|strcat|strncat|memcpy)" if search_printf else "(exec|system|strcpy|argv|gets|read|strncpy|popen|strcat|strncat|memcpy)"
        m = re.search(regex,line)
        if m:
            print(len(path) * '---', os.path.basename(srcfile.name), 'line', cnt, line)
        cnt = cnt+1

if __name__ == "__main__":
    search_printf = False
    if len(sys.argv) == 1:
        print("Please add provide directory name as first argument")
        sys.exit()
    elif len(sys.argv) == 2: 
        rootpath = sys.argv[1]
        print("Enable searching printf. Pass 'y' as second argument")
    elif len(sys.argv) == 3: 
        rootpath = sys.argv[1]
        if sys.argv[2] == 'y':
            search_printf = True
    for root, dirs, files in os.walk(rootpath):
        path = root.split(os.sep)
        print((len(path) - 1) * '---', os.path.basename(root))
        for file in files:
    	    if file.endswith('.c'):
                with open(os.path.join(root,file),'r') as srcfile:
                   analyze(path, srcfile, search_printf)
