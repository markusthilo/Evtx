#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Markus Thilo'
__version__ = '0.1_2021-02-08'
__license__ = 'GPL-3'

from Evtx import Evtx
from bs4 import BeautifulSoup
from argparse import ArgumentParser, FileType
from sys import stdout as StdOut
from sys import stderr as StdErr
from sys import exit as SysExit

if __name__ == '__main__':	# start here if called as application
	argparser = ArgumentParser(description='Analize netflow data')
#	argparser.add_argument('-n', '--noheadline', action='store_true',
#		help='Suppress headlines = column names on CSV output'
#	)
#	argparser.add_argument('-t', '--type', dest='datatype',
#		help='Type of input data and calculation - use -t l or -t list to get details',
#		metavar='STRING'
#	)
#	argparser.add_argument('-u', '--unixtime', action='store_true',
#		help='Unix timestamps (seconds and microseconds) on CSV output'
#	)
#	argparser.add_argument('-v', '--verbose', action='store_true',
#		help='Verbose output'
#	)
	argparser.add_argument('-w', '--outfile', type=FileType('w'),
		help='File to write', metavar='FILE', default=StdOut
	)	
	argparser.add_argument('infile', nargs=1, type=FileType('rt'),
		help='Event log file to read', metavar='FILE'
	)
	args = argparser.parse_args()
	print(args.infile)
	with Evtx.Evtx(args.infile[0].name) as logfile:
		for record in logfile.records():
			print('------------------------------------------')
			bs = BeautifulSoup(record.xml())
			print(bs)

	SysExit(0)

