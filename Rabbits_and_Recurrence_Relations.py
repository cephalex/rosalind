import sys

if len(sys.argv) < 3:
    print("Specify n then k")
    sys.exit(1)

n = int(sys.argv[1])
k = int(sys.argv[2])

print("n = {}, k = {}".format(n, k))

def rabbits(n, k):
    print("Rabbits n = {}, k = {}".format(int(n), int(k)))
    if n <= 0:
        print("Returning 0")
        return 0
    elif n == 1:
        print("Returning 1")
        return (1)
    elif n == 2:
        print("Returning {}".format(k+1))
        return (k+1)
    else:
        return (rabbits(n-2, k) + rabbits(n-1, k))

def rabbits_iterative(n, k):
    total = 1
    for i in range (abs(n)):
        total = total + (total * k)
        print("total = {}".format(total))
    return (total)


def fib(n):
#    print("fib n = {}".format(n))
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fib(n-1) + fib(n-2))

# output
print ("Rabbits({} , {}) = {}".format(n, k, rabbits(n, k)))

print("Fibonacci({}) = {}".format(n, fib(n)))

print("Rabbits Iterative({} , {}) = {}".format(n, k, rabbits_iterative(n,k)))
