#!/usr/bin/evn python

import glob
import os
rule_file = open("final_binders.txt", "r")

lines = rule_file.readlines()
rule_file.close()
mol_name = []
for line in lines:
    cor_isomer = line.split()[1]
    mol_name.append(cor_isomer + ".mol2")

print mol_name
sub_files = glob.glob("*.mol2")

count = []
for file in sub_files:
    if file in mol_name:
        print file
        count.append(file)
    else:
        os.remove(file)
print len(count)
