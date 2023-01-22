import sys, getopt

help_info = "main.py -i <inputDir> -o <outputDir>"
input_dir = ""
output_dir = ""

try:
    opts = getopt.getopt(sys.argv[1:],"hi:o:")[0]
except getopt.GetoptError:
    print (help_info)
    sys.exit()

if len(opts) == 0:
    print (help_info)
    sys.exit()

for opt, arg in opts:
    if opt == "-h":
        print (help_info)
        sys.exit()
    elif opt == "-i":
        input_dir = arg
    elif opt == "-o":
        output_dir = arg
    