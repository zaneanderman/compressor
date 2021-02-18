#!/usr/bin/python3
import string
import sys
import re
from collections import defaultdict
import copy

decompflags = ""
availablechrs = []
for i in range(161, 256):
	availablechrs.append(chr(i))

frequencies = defaultdict(lambda:0)
with open(sys.argv[1], "r") as f:
	text = f.read()
splittext = re.split("\W+", text)

for word in splittext:
	frequencies[word] += 1


freqcpy = copy.copy(frequencies)
for i in freqcpy.items():
	if not (i[1] >= 2 and len(i[0]) > 1):
		del frequencies[i[0]]

freqcpy = copy.copy(frequencies)
while len(frequencies) >= 95:
	frequencies.popitem()

counter = 0
for i in frequencies.keys():
	text = text.replace(i, availablechrs[counter])
	counter += 1
	decompflags += f"{i} {availablechrs[counter]} "

text = decompflags + "\n" + text

with open(sys.argv[1]+".cmp", "w") as f:
	f.write(text)

"""
for i in range(161, 256):
	print(chr(i))
"""

