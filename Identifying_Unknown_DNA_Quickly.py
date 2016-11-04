import sys

if len(sys.argv) < 2:
    print("No data file specified")
    sys.exit(1)

def calc_gc_content(seq):
    gc = 0
    for letter in seq:
        if ((letter == 'G') or (letter == 'C')):
            gc = gc + 1
    print("calc_gc_content:len(seq) = {}".format(len(seq)))
    print("calc_gc_content:gc = {}".format(gc))
    if len(seq) == 0:
        return 0
    else:
        return (gc / len(seq)) * 100

# read in data
data_file = open(sys.argv[1], 'r')

# crunch data
gc_list = []
seq_name = ""
seq = ""
for line in data_file:
    print("line = {}".format(line))
    gc_content = calc_gc_content(seq)
    print("gc_content = {}".format(gc_content))
    if line[0] == '>':
        print("old seq_name = {}".format(seq_name))
        print("old seq = {}".format(seq))
        gc_list.append((seq_name, round(gc_content,6)))
        seq_name = line[1:].rstrip()
        print ("seq_name = {}".format(seq_name))
        seq = ""
    else:
        seq = seq + line.rstrip()
        print ("seq = {}".format(seq))
        print ("len(seq) = {}".format(len(seq)))

gc_content = calc_gc_content(seq)
gc_list.append((seq_name, round(gc_content,6)))

data_file.close()


# output
print (gc_list)

greatest_gc = gc_list[0]
for pair in gc_list:
    print("pair = {}".format(pair))
    if pair[1] > greatest_gc[1]:
#    if pair[1] > 0:
        greatest_gc = pair

print ("greatest_gc:")
print ("{}".format(greatest_gc[0]))
print ("{}".format(greatest_gc[1]))
