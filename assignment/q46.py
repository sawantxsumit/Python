try:
    num = float(input("Enter a number: "))
    if num < 0:
        raise ValueError("Negative number entered!")
    print(f"The entered number is: {num}")
except ValueError as ve:
    print(f"Exception: {ve}")

