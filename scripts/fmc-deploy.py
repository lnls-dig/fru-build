#!/usr/bin/python

import os
import argparse
from subprocess import call
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('-s','--start', required=True, help='Starting Serial Number of FMC list')
parser.add_argument('-e','--end', required=True, type=str, help='Ending Serial Number of FMC list')
parser.add_argument('-d','--dir', type=str, default=os.getcwd()+'/fmc_bin', help='Output directory for binary files')
args = parser.parse_args()

sn_start = int(args.start)
sn_end = int(args.end)

#Create output dir
if os.path.exists(args.dir):
    shutil.rmtree(args.dir)
os.makedirs(args.dir)

for sn in range(sn_start, sn_end+1, 1):
    cur_sn = str(sn)
    call(["../fmc_fru "+args.dir+"/fmc_250_"+cur_sn+".bin \""+cur_sn+"\""], shell=True)
