# collections.Counter()

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

__[collections.Counter()](https://docs.python.org/2/library/collections.html#collections.Counter)__  
 A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
 
 <sub> __Sample Code__ </sub>
 
    >>> from collections import Counter
    >>> 
    >>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
    >>> print Counter(myList)
    Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
    >>>
    >>> print Counter(myList).items()
    [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
    >>> 
    >>> print Counter(myList).keys()
    [1, 2, 3, 4, 5]
    >>> 
    >>> print Counter(myList).values()
    [3, 4, 4, 2, 1]

---
__Task__

$Raghu$ is a shoe shop owner. His shop has $X$ number of shoes.  
He has a list containing the size of each shoe he has in his shop.  
There are $N$ number of customers who are willing to pay $x_i$ amount of money only if they get the shoe of their desired size.

Your task is to compute how much money $Raghu$ earned.

**Input Format**

The first line contains $X$, the number of shoes.  
The second line contains the space separated list of all the shoe sizes in the shop.<br>
The third line contains $N$, the number of customers.  
The next $N$ lines contain the space separated values of the $shoe \ size$ desired by the customer and $x_i$, the price of the shoe.

__Constraints__

$0 < X < 10^3$  
$0 < N \le 10^3$  
$20 < x_i < 100$  
$ 2 < shoe \ size < 20 $
 

**Output Format**

 Print the amount of money earned by $Raghu$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-22T19:51:06.627Z  

```py
from collections import Counter

# Read the number of shoes
num_shoes = int(input())

# Read the shoe sizes and create a Counter dictionary
shoe_sizes = Counter(map(int, input().split()))

# Read the number of customers
num_customers = int(input())

total_earned = 0

# Process each customer's request
for _ in range(num_customers):
    size, price = map(int, input().split())
    
    # If the shoe size is available in inventory
    if shoe_sizes[size] > 0:
        total_earned += price
        shoe_sizes[size] -= 1

# Print the total amount of money earned
print(total_earned)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/collections-counter/problem)