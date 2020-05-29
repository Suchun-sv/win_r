#encoding:utf-8
from ruamel.yaml import YAML
import os
import re
import sys
import argparse
import os
import win32com.client as client

shell = client.Dispatch("WScript.Shell")
parser = argparse.ArgumentParser()
parser.add_argument("targetDir")
parser.add_argument('-p', '--parent', help="add a Dir to baseDirs")
parser.add_argument('-s', '--select', help="select the default parent folder to in generating file", action="store_true")
parser.add_argument('-m', '--mklink', nargs='*',help="created shortcut of the file")
parser.add_argument('--debug', help="show args", action="store_true")

args = parser.parse_args()

yaml = YAML()
if args.debug:
    print(args)
with open(os.environ['FileCMD']+'\config.yml', "r",encoding='utf-8') as file:
    data = yaml.load(file.read())  

if "BaseDirs" in data.keys():
    BaseDirs = data['BaseDirs']
else:
    BaseDirs = list()
    
if "CurrentDir" in data.keys():
    CurrentDir = data['CurrentDir']
    
if args.select:
    for index,Dir in enumerate(BaseDirs):
        print(f"{index}\t{Dir}")

    while True:
        index = eval(input("select the default parent path:"))
        try:
            CurrentDir = BaseDirs[index]
            break
        except IndexError:
            print(f"index shoule be in the range of {len(Base_Dirs)-1}")
            
if args.parent:
    NewParentDir = args.parent
    if os.path.exists(NewParentDir):
        if not os.path.isabs(NewParentDir):
            NewParentDir = os.path.abspath(NewParentDir)
        if NewParentDir not in BaseDirs:
            BaseDirs.append(NewParentDir)
        CurrentDir = NewParentDir
        print("{} has been set to default parent dir!".format(CurrentDir))
    else:
        print("FILE Not EXIST!")
        sys.exit()


targetDir = args.targetDir
# find the maxIndex in the currentDir
flag = 0
if 1:
    x = re.compile("^\d\d .*")
    maxIndex = 0
    for path in os.listdir(CurrentDir):
        if re.findall(x, path):
            flag = 1
            maxIndex = max(maxIndex, int(path[:2]))
# if maxIndex not zero ,plus one.
if flag == 1:
    maxIndex = maxIndex+1
# make the appropriate folderName
mkpath = os.path.join(CurrentDir, "{:02} {}".format(maxIndex,targetDir))
# make dir

os.mkdir(mkpath)
print("{} created!".format(mkpath)) 

data = {
    "BaseDirs":BaseDirs,
    "CurrentDir":CurrentDir
       }
      
        
# save config.yml
with open(os.environ['FileCMD']+'\config.yml', "w",encoding='utf-8') as file:
    yaml.dump(data, file)  


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
    
if args.mklink:
    new_map = dict()
    parentPath = os.environ['FileCMD']
    with open(os.path.join(parentPath, "map/map.yml"), "r", encoding="utf-8") as f:
        maps = yaml.load(f)
    for link in args.mklink:
       if link not in maps.keys():
        CreateShortCut(mkpath, "{}/links/{}.lnk".format(parentPath, link))
        new_map[link] = mkpath
        maps[link] = mkpath
       else:
        print("{} has been set to {}".format(link, maps[link]))
        
    with open(os.path.join(parentPath, "map/map.yml"), "w", encoding="utf-8") as f:
        yaml.dump(maps, f)
        
    