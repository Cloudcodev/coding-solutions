# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

# Read input from STDIN
s, k = input().split()

# Print permutations in lexicographic sorted order
for p in permutations(sorted(s), int(k)):
    print("".join(p))
