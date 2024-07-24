import csv
import sys

def main():
    # Ensure correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python dna.py <database.csv> <sequence.txt>")
        sys.exit(1)

    # Read database file into a list of dictionaries
    database_file = sys.argv[1]
    dna_sequence_file = sys.argv[2]

    with open(database_file) as file:
        reader = csv.DictReader(file)
        database = [row for row in reader]
        str_names = reader.fieldnames[1:]  # Exclude the first column (name)

    # Read DNA sequence from file
    with open(dna_sequence_file) as file:
        dna_sequence = file.read().strip()

    # Find longest match of each STR in DNA sequence
    str_counts = {}
    for str_name in str_names:
        str_counts[str_name] = longest_match(dna_sequence, str_name)

    # Check database for matching profiles
    for person in database:
        match = all(int(person[str_name]) == str_counts[str_name] for str_name in str_names)
        if match:
            print(person["name"])
            return

    print("No match")

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    for i in range(sequence_length):
        count = 0
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        longest_run = max(longest_run, count)

    return longest_run

if __name__ == "__main__":
    main()
