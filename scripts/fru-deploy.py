#!/usr/bin/python
import os
import argparse
from subprocess import call
import shutil
from datetime import datetime
import re


lastNum = re.compile(r'(?:[^\d]*(\d+)[^\d]*)+')
#Code from Chris Olds @ http://code.activestate.com/recipes/442460/
def increment(s):
    """ look for the last sequence of number(s) in a string and increment """
    m = lastNum.search(s)
    if m:
        next = str(int(m.group(1))+1)
        start, end = m.span(1)
        s = s[:max(end-len(next), start)] + next + s[end:]
    return s

parser = argparse.ArgumentParser()
parser.add_argument('-b','--board', required=True, choices=['afc','amc','fmc','rtm'], help='Board type')
parser.add_argument('-s','--start', required=True, help='Starting Serial Number of board list')
parser.add_argument('-e','--end', required=True, type=str, help='Ending Serial Number of board list')
parser.add_argument('-d','--dir', type=str, default=os.getcwd()+'/fru_bin', help='Output directory for binary files')
parser.add_argument('-t','--time', type=str, default='01/01/2017', help='Board manufacturing date (DD/MM/YYYY)')
args = parser.parse_args()

if args.board == 'afc':
    args.board = 'amc'

orig_time = datetime.strptime('01/01/1996', '%d/%m/%Y')
manuf_time = datetime.strptime(args.time, '%d/%m/%Y')
delta_min = (manuf_time-orig_time).total_seconds()/60.0

#Create output dir
if os.path.exists(args.dir):
    shutil.rmtree(args.dir)
os.makedirs(args.dir)

cur_sn = args.start
while True:
    call(["../{}_fru {}/{}.bin \"{}\" {}".format(args.board, args.dir, cur_sn, cur_sn, delta_min)], shell=True)
    if cur_sn == args.end:
        break
    else:
        cur_sn = increment(cur_sn)
