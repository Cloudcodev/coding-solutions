# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

# Read the complex number input
z = complex(input().strip())

# Print absolute value (r) and phase (phi)
print(abs(z))
print(cmath.phase(z))
