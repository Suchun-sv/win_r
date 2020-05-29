#encoding:utf-8
from ruamel.yaml import YAML
import os
import argparse
import pyperclip
yaml = YAML()
#shell = client.Dispatch("WScript.Shell")
parser = argparse.ArgumentParser()
parser.add_argument('destination', help="copy the destination path to clipboard")
args = parser.parse_args()
parentPath = os.environ['FileCMD']
with open(os.path.join(parentPath, "map/map.yml"), "r", encoding="utf-8") as f:
    maps = yaml.load(f)
if args.destination in maps.keys():
    pyperclip.copy(maps[args.destination])
    print("\""+maps[args.destination]+"\""+" has been paste to clipboard!")
    
        

        
    