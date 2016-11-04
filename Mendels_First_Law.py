import sys

if len(sys.argv) < 4:
    print("usage: python3 Mendels_First_Law k m n")
    sys.exit(1)

k = int(sys.argv[1])
m = int(sys.argv[2])
n = int(sys.argv[3])
total = k + m + n

if (k < 0) or (m < 0) or (n < 0):
    print("k, m, or n cannot be less than zero")
    sys.exit(1)

if (total*total - total == 0):
    print("0")
    sys.exit(1)

print("k = {}, m = {}, n = {}".format(k, m, n))

print((k * (k + 2*m + 2*n - 1) + m*n + 0.75*(m*m - m))/(total*total - total))
