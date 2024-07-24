from cs50 import get_float

# Prompt user for the amount of change owed
while True:
    change = get_float("Change : ")
    if change > 0:
        break

# Convert dollars to cents
cents = round(change * 100)

# Initialize coin count
coins = 0

# Calculate the minimum number of coins
for coin in [25, 10, 5, 1]:
    coins += cents // coin
    cents %= coin

# Print the result
print(coins)

