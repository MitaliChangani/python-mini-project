def sum(n):
    # Base case: if n is a single digit, return the number itself
    if n < 10:
        return n
    # Recursive case: sum the last digit and the sum of digits of the rest of the number
    else:
        return n % 10 + sum(n // 10)

# Test the function
n = int(input("Enter a number: "))
result = sum(n)
print(f"The sum of digits in {n} is {result}")
