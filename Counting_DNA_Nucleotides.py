import sys

data_file = open('workfile', 'r')

data = data_file.read(1000)

Adenine = 0
Guanine = 0
Cytosine = 0
Thymine = 0

for letter in data:
    if letter == 'A':
        Adenine += 1
    elif letter == 'G':
        Guanine += 1
    elif letter == 'C':
        Cytosine += 1
    elif letter == 'T':
        Thymine += 1

print ("{} {} {} {}".format(Adenine, Cytosine, Guanine, Thymine))

data_file.close()
