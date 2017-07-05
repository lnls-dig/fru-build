#!/usr/bin/python

import os
import argparse
from subprocess import call
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('-b','--board', required=True, choices=['afc','amc','fmc'], help='Board type')
parser.add_argument('-s','--start', required=True, help='Starting Serial Number of board list')
parser.add_argument('-e','--end', required=True, type=str, help='Ending Serial Number of board list')
parser.add_argument('-d','--dir', type=str, default=os.getcwd()+'/fru_bin', help='Output directory for binary files')
args = parser.parse_args()

sn_start = int(args.start)
sn_end = int(args.end)

if args.board == 'afc':
    args.board = 'amc'

#Create output dir
if os.path.exists(args.dir):
    shutil.rmtree(args.dir)
os.makedirs(args.dir)

for sn in range(sn_start, sn_end+1, 1):
    cur_sn = str(sn)
    call(["../"+args.board+"_fru "+args.dir+"/"+args.board+"_"+cur_sn+".bin \""+cur_sn+"\""], shell=True)
