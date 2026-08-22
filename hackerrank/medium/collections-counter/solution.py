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
