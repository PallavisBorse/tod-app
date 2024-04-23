# Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Input number from user
num = int(input("Enter a number: "))

# Calculate and print factorial
print("Factorial of", num, "is", factorial(num))

