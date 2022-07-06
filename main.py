from BtLang import *
from sys import *

filename = argv[1]

file = open(filename, "r").read()

try:
    exec(file)
except:
    print("Error")
