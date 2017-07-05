#!/usr/bin/python

import os
import sys
import time
from time import sleep
import argparse
from string import split
from subprocess import call
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('-s','--start', required=True, help='Starting Serial Number of RFFE list')
parser.add_argument('-e','--end', required=True, type=str, help='Ending Serial Number of RFFE list')
args = parser.parse_args()

net_prefix = ".".join(split(args.start,'.')[0:3])+'.'
sn_start = int(args.start)
sn_end = int(args.end)

tmp_folders=[]

#Create output dir
out_folder = os.getcwd()+"/bin"
if os.path.exists(out_folder):
    shutil.rmtree(out_folder)
os.makedirs(out_folder)

for sn in range(sn_start, sn_end+1, 1):
    cur_sn = str(sn)
    try:
        cur_folder = os.getcwd()+"/openMMC/out_"+cur_sn
        if os.path.exists(cur_folder):
            shutil.rmtree(cur_folder)
        os.makedirs(os.getcwd()+"/openMMC/out_"+cur_sn)
        print(os.getcwd()+"/openMMC/out_"+cur_sn)
        tmp_folders.append(cur_folder)
    except OSError:
        if not os.path.isdir(cur_folder):
            raise
        pass

    call(["cd "+cur_folder+" && cmake ../ -DBOARD=afc-bpm -DVERSION=3.1 -DCMAKE_BUILD_TYPE=Debug -DAMC_SN=\""+cur_sn+"\" && make full_binary"], shell=True)
    #print("cd "+cur_folder+" && cmake ../ -DBOARD=afc-bpm -DVERSION=3.1 -DCMAKE_BUILD_TYPE=Debug -DAMC_SN=\""+cur_sn+"\" && make full_binary")
    call(["mv "+cur_folder+"/out/openMMC_full.bin "+out_folder+"/openMMC_"+cur_sn+".bin"], shell=True)


for fold in tmp_folders:
    shutil.rmtree(fold)
