import sys


f = open(sys.argv[1], 'r')
contents = f.read()
print(contents)
f.close() 
