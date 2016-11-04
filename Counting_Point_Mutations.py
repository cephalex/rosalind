import sys

if len(sys.argv) < 2:
    print("No data file specified")
    sys.exit(1)

# read in data
data_file = open(sys.argv[1], 'r')
seq1 = data_file.readline().rstrip()
seq2 = data_file.readline().rstrip()

mismatches = 0
n = 0

for letter1 in seq1:
    if letter1 != seq2[n]:
        mismatches = mismatches + 1
    n = n + 1

print (mismatches)
