def count_characters(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    lower = upper = digit = special = 0

    for char in data:
        if char.islower():
            lower += 1
        elif char.isupper():
            upper += 1
        elif char.isdigit():
            digit += 1
        else:
            special += 1

    print(f"Lowercase letters: {lower}")
    print(f"Uppercase letters: {upper}")
    print(f"Digits: {digit}")
    print(f"Special symbols: {special}")

# Example usage
file_path = 'file1.txt'  # Replace with your file name
count_characters(file_path)
