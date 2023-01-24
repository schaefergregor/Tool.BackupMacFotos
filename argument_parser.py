"""
Module to parse arguments.
"""
import sys
import getopt

HELP_INFO = "main.py -i <inputDir> -o <outputDir>"
INPUT_DIR = ""
OUTPUT_DIR = ""

try:
    opts = getopt.getopt(sys.argv[1:],"hi:o:")[0]
except getopt.GetoptError:
    print (HELP_INFO)
    sys.exit()

if len(opts) == 0:
    print (HELP_INFO)
    sys.exit()

for opt, arg in opts:
    if opt == "-h":
        print (HELP_INFO)
        sys.exit()
    elif opt == "-i":
        INPUT_DIR = arg
    elif opt == "-o":
        OUTPUT_DIR = arg
    