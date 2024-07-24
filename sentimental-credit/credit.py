from cs50 import get_string

# Prompt user for credit card number
card_number = get_string("Number: ")

# Function to check Luhn's Algorithm
def check_luhn(card):
    total_sum = 0
    reversed_card = card[::-1]
    for i, digit in enumerate(reversed_card):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total_sum += n
    return total_sum % 10 == 0

# Function to determine card type
def get_card_type(card):
    if (len(card) == 15 and (card.startswith("34") or card.startswith("37"))):
        return "AMEX"
    elif (len(card) == 16 and card.startswith("5") and card[1] in "12345"):
        return "MASTERCARD"
    elif (len(card) in [13, 16] and card.startswith("4")):
        return "VISA"
    else:
        return "INVALID"

# Validate the card
if check_luhn(card_number):
    card_type = get_card_type(card_number)
else:
    card_type = "INVALID"

# Print the result
print(card_type)
