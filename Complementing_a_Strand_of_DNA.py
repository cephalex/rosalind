import sys

if len(sys.argv) < 2:
    print("No data file specified")
    sys.exit(1)

# read in data
data_file = open(sys.argv[1], 'r')
data = data_file.read(1000)
data_file.close()
print("data_file = {}".format(data))

# output
print (data.replace('T','a').replace('A','T').replace('a', 'A').replace('C','g').replace('G','C').replace('g', 'G')[::-1])
