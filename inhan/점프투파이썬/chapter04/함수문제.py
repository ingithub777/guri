import sys

args=sys.argv[1:]
for i in args:
    print("Hello,",str(i[0]).upper()+i[1:],end='')