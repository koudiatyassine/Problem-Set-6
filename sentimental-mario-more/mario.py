from cs50 import get_int

# Prompt user for the height of the pyramid
while True:
    height = get_int("Height: ")
    if 1 <= height <= 8:
        break

# Print the double half-pyramid
for i in range(1, height + 1):
    # Print left half-pyramid
    print(" " * (height - i) + "#" * i, end="")
    # Print gap
    print("  ", end="")
    # Print right half-pyramid
    print("#" * i)
