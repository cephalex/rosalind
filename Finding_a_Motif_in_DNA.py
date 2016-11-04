import sys

def findall(seq, motif, start):
  index = int(seq.find(motif,start))
  if index != -1:
    print("{}".format(index+1), end=' ')
  if len(seq) > index and index != -1:
    findall(seq, motif, index+1)
  return

if len(sys.argv) < 2:
    print("No data file specified")
    sys.exit(1)

# read in data
data_file = open(sys.argv[1], 'r')
s = data_file.readline(10000).rstrip()
t = data_file.readline(10000).rstrip()
data_file.close()

#process and output 
findall(s, t, 0)

print()

