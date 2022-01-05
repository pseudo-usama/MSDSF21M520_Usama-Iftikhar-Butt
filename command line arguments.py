import sys
import getopt


print(sys.argv)
print(getopt.getopt(sys.argv[1:], 'a:b:'))
