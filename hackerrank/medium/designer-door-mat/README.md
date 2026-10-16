# Designer Door Mat

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications: 

- Mat size must be $N  $X$  M$. ($N$ is an odd natural number, and $M$ is $3$ times $N$.)
- The design should have 'WELCOME' written in the center.
- The design pattern should only use `|`, `.` and `-` characters.

__Sample Designs__

```
    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
```    



**Input Format**

A single line containing the space separated values of $N$ and $M$.  


**Constraints**

+ $5 < N < 101$
+ $15 < M < 303$

**Output Format**

Output the design pattern.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-16T19:55:07.573Z  

```py
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

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/designer-door-mat/problem)