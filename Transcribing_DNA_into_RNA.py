import sys

if len(sys.argv) < 2:
    print("No data file specified")
    sys.exit(1)

data_file = open(sys.argv[1], 'r')

data = data_file.read(1000)

data_file.close()

print (data.replace('T','U'))
