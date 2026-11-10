# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

# Read input lists A and B from STDIN
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Compute the cartesian product and print space-separated tuples
print(*product(A,B))
