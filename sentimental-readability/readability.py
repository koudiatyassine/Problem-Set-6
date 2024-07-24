from cs50 import get_string
import re

def count_letters(text):
    return len(re.findall(r'[a-zA-Z]', text))

def count_words(text):
    return len(re.findall(r'\b\w+\b', text))

def count_sentences(text):
    return len(re.findall(r'[.!?]', text))

# Prompt user for text
text = get_string("Text: ")

# Calculate counts
letters = count_letters(text)
words = count_words(text)
sentences = count_sentences(text)

# Calculate Coleman-Liau index
L = (letters / words) * 100
S = (sentences / words) * 100
index = 0.0588 * L - 0.296 * S - 15.8

# Determine grade level
if index < 1:
    grade = "Before Grade 1"
elif index >= 16:
    grade = "Grade 16+"
else:
    grade = f"Grade {round(index)}"

# Print the result
print(grade)
