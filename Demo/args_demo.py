import sys

#print(sys.argv)
#print(sys.argv[1])

import getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], "a:b:c", ["add=", "delete="])
except getopt.GetoptError: 
    print('usage: args_demo.py -a arg1 -b arg2 -c --add arg3 --delete arg4')
    sys.exit()
#print(sys.argv)
print(opts)
#print(len(sys.argv) - 1)
