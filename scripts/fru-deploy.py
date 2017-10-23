#!/usr/bin/python

import os
import argparse
from subprocess import call
import shutil
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-b','--board', required=True, choices=['afc','amc','fmc'], help='Board type')
parser.add_argument('-s','--start', required=True, help='Starting Serial Number of board list')
parser.add_argument('-e','--end', required=True, type=str, help='Ending Serial Number of board list')
parser.add_argument('-d','--dir', type=str, default=os.getcwd()+'/fru_bin', help='Output directory for binary files')
parser.add_argument('-t','--time', type=str, default='01/01/2017', help='Board manufacturing date (DD/MM/YYYY)')
args = parser.parse_args()

sn_start = int(args.start)
sn_end = int(args.end)

if args.board == 'afc':
    args.board = 'amc'

orig_time = datetime.strptime('01/01/1996', '%d/%m/%Y')
manuf_time = datetime.strptime(args.time, '%d/%m/%Y')
delta_min = (manuf_time-orig_time).total_seconds()/60.0

#Create output dir
if os.path.exists(args.dir):
    shutil.rmtree(args.dir)
os.makedirs(args.dir)

for sn in range(sn_start, sn_end+1, 1):
    cur_sn = str(sn)
    call(["../{}_fru {}/{}_{}.bin \"{}\" {}".format(args.board, args.dir, args.board, cur_sn, cur_sn, delta_min)], shell=True)
