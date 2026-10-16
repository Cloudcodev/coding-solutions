# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read space-separated integers N and M from standard input
N, M = map(int, input().split())

# Top half of the door mat
for i in range(1, N, 2):
    pattern = ('.|.' * i).center(M, '-')
    print(pattern)

# Middle row containing 'WELCOME'
print('WELCOME'.center(M, '-'))

# Bottom half of the door mat (mirror image of top half)
for i in range(N - 2, 0, -2):
    pattern = ('.|.' * i).center(M, '-')
    print(pattern)
