import sys

codon_dict = {"UUU": 'F', "CUU": 'L', "AUU": 'I', "GUU": 'V',
              "UUC": 'F', "CUC": 'L', "AUC": 'I', "GUC": 'V',
              "UUA": 'L', "CUA": 'L', "AUA": 'I', "GUA": 'V',
              "UUG": 'L', "CUG": 'L', "AUG": 'M', "GUG": 'V',
              "UCU": 'S', "CCU": 'P', "ACU": 'T', "GCU": 'A',
              "UCC": 'S', "CCC": 'P', "ACC": 'T', "GCC": 'A',
              "UCA": 'S', "CCA": 'P', "ACA": 'T', "GCA": 'A',
              "UCG": 'S', "CCG": 'P', "ACG": 'T', "GCG": 'A',
              "UAU": 'Y', "CAU": 'H', "AAU": 'N', "GAU": 'D',
              "UAC": 'Y', "CAC": 'H', "AAC": 'N', "GAC": 'D',
              "UAA": 'Stop', "CAA": 'Q', "AAA": 'K', "GAA": 'E',
              "UAG": 'Stop', "CAG": 'Q', "AAG": 'K', "GAG": 'E',
              "UGU": 'C', "CGU": 'R', "AGU": 'S', "GGU": 'G',
              "UGC": 'C', "CGC": 'R', "AGC": 'S', "GGC": 'G',
              "UGA": 'Stop', "CGA": 'R', "AGA": 'R', "GGA": 'G',
              "UGG": 'W', "CGG": 'R', "AGG": 'R', "GGG": 'G'};

def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

if len(sys.argv) < 2:
    print("No data file specified")
    sys.exit(1)

# read in data
data_file = open(sys.argv[1], 'r')
data = data_file.read(10000).rstrip()
data_file.close()
print("data_file = {}".format(data))

# check data if complete codons
if (len(data) % 3) != 0:
	print("Data has incomplete codons, length = {}".format(len(data)))
	sys.exit(1)

# split into codons
codons = chunks(data, 3)
#for codon in codons:
#	print("codon = {}".format(codon))

proteins = ''
for codon in codons:
	proteins = proteins + codon_dict[codon]
#	print("Proteins = {}".format(proteins))
     
# output protein sequence
print("Proteins = {}".format(proteins))

