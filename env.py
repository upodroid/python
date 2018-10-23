import sys,re,socket

file = open(sys.argv[1], 'r')

for line in file:
    if re.match("(.*)HOME(.*)", line):
        print(line.rstrip())
    if re.match("PWD(.*)", line):
        print(line.rstrip())
    if re.match("(.*)SHELL(.*)", line):
        print(line.rstrip())
    if re.match("(.*)USER(.*)", line):
        print(line.rstrip())
print("HOST=",socket.gethostname())
file.close()

