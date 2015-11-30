# -*- coding:utf-8 -*-
# author:sundayliu
# date:2015.11.30

import os,sys

from Npp import notepad

def convert2uft8(filename):
    #print filename
    filename = filename.encode("UTF-8")
    notepad.open(filename)
    notepad.runMenuCommand("Encoding", "Convert to UTF-8")
    notepad.save()
    notepad.close()
    print filename

def do_main(root_path):
        # print root_path
        names = os.listdir(root_path)
        for name in names:
            full_path = os.path.join(root_path, name)
            if os.path.isdir(full_path):
                do_main(full_path)
            
            else:
                full_path = full_path.decode("GBK")
                if full_path.endswith(u".txt"):
                    convert2uft8(full_path)
                
root_dir = "e:\\reader\\data"
# print root_dir
do_main(root_dir)

