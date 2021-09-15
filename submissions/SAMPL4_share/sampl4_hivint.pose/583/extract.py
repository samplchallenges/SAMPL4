#!/usr/bin/evn python

import glob 
import commands
file_type = "pdb"
files = glob.glob("*.%s"%file_type)
target = "MOL"

for file in files:
    new_file = "new" + file
    target_lines = commands.getoutput("grep %s %s > %s"%(target, file, new_file))
    commands.getoutput("mv %s %s" %(new_file, file))
