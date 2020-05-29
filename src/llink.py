#encoding:utf-8
from ruamel.yaml import YAML
import os
import re
import sys
import argparse
import os
import win32com.client as client
yaml = YAML()
shell = client.Dispatch("WScript.Shell")
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--show', help="show the shortcuts to the pwd folders", action="store_true")
#parser.add_argument('-d', '--destination', nargs='*',help="specify the target file")
parser.add_argument('-m', '--mklink', nargs='*',help="created shortcut of the destination file")
parser.add_argument('-rm', '--remove', help="remove the shortcut of the current folder", action="store_true")
parser.add_argument('--debug', help="show args", action="store_true")
args = parser.parse_args()


#links 
def GetShortCut(shortcut):
    return shell.CreateShortCut(shortcut).Targetpath

def createShortCut(filename, lnkname):
    """filename should be abspath, or there will be some strange errors"""
    shortcut = shell.CreateShortCut(lnkname)
    shortcut.TargetPath = filename
    shortcut.save()

def CreateShortCut(filename, lnkname):
    createShortCut(os.path.abspath(filename), lnkname)
currentPath = os.getcwd()
parentPath = os.environ['FileCMD']

def show_currentPath(currentPath):
    with open(os.path.join(parentPath, "map/map.yml"), "r", encoding="utf-8") as f:
        maps = yaml.load(f)   
    reverseMap = dict()
    for value,key in maps.items():
        if key not in reverseMap.keys():
            reverseMap[key] = list()
            reverseMap[key].append(value)
        else:
            reverseMap[key].append(value)
    if args.debug:
        print(reverseMap.items())
    if currentPath in reverseMap.keys():
        for lnkname in reverseMap[currentPath]:
            print(lnkname,end=" ")
#if args.show:
 #   show_currentPath(currentPath)

        #print("\n")
        
if args.mklink:
    new_map = dict()
    parentPath = os.environ['FileCMD']
    with open(os.path.join(parentPath, "map/map.yml"), "r", encoding="utf-8") as f:
        maps = yaml.load(f)
    for link in args.mklink:
       if link not in maps.keys():
        CreateShortCut(currentPath, "{}/links/{}.lnk".format(parentPath, link))
        maps[link] = currentPath
       else:
           while True:
                selected = input("{} has been set to {}, override it?(y/n)".format(link, maps[link]))
                if selected == '' or selected == 'y' or selected =='Y':
                    CreateShortCut(currentPath, "{}/links/{}.lnk".format(parentPath, link))
                    maps[link] = currentPath
                    break
                elif selected=='N' or selected =='n':
                    break
    with open(os.path.join(parentPath, "map/map.yml"), "w", encoding="utf-8") as f:
        yaml.dump(maps, f)

if args.remove:
    parentPath = os.environ['FileCMD']
    with open(os.path.join(parentPath, "map/map.yml"), "r", encoding="utf-8") as f:
        maps = yaml.load(f)  
   
    reverseMap = dict()
    for value,key in maps.items():
        if key not in reverseMap.keys():
            reverseMap[key] = list()
            reverseMap[key].append(value)
        else:
            reverseMap[key].append(value)
    if args.debug:
        print(reverseMap.items())
    if currentPath in reverseMap.keys():
        for lnkname in reverseMap[currentPath]:
            maps.pop(lnkname)
    with open(os.path.join(parentPath, "map/map.yml"), "w", encoding="utf-8") as f:
        yaml.dump(maps, f)
        
show_currentPath(currentPath)
        
    