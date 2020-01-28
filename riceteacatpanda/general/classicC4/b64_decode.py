#! python3
import base64

f = open('daBomb.txt', 'r')
f = f.readlines()

for line in f:
	print(base64.b64decode(line))