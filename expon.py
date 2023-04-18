# Set initial variables
amount = 0.01
days = 30

# Calculate the amount after 30 days
for i in range(days):
    amount *= 2

# Print the final amount
print(round(amount, 2))

# Output: 10737418.24

"""
You are offered a choice of either $1.000.000 or $0.01 (one penny) doubled every day for 30 days (the resulting amount is doubled every day).

Task:
Write a program to calculate the amount that will result from the doubling to understand which choice results in a larger amount.
"""
