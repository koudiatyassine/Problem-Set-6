from cs50 import get_int

# Prompt user for the height of the pyramid
while True:
    height = get_int("Height: ")
    if 1 <= height <= 8:
        break

# Print the half-pyramid
for i in range(1, height + 1):
    # Print spaces
    print(" " * (height - i), end="")
    # Print hashes
    print("#" * i)

