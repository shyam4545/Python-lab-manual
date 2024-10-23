import math
import random

while True:
    print("\nOptions:")
    print("1. Square root")
    print("2. Factorial")
    print("3. Random number")
    print("4. Exit")

    choice = int(input("Choose an option (1-4): "))

    if choice == 1:
        num = float(input("Enter a non-negative number: "))
        if num < 0:
            print("Error: Cannot calculate square root of a negative number.")
        else:
            print(f"Square root of {num} is {math.sqrt(num)}")

    elif choice == 2:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            print(f"Factorial of {num} is {math.factorial(num)}")

    elif choice == 3:
        lower = int(input("Enter lower bound: "))
        upper = int(input("Enter upper bound: "))
        if lower >= upper:
            print("Error: Lower bound must be less than upper bound.")
        else:
            print(f"Random number between {lower} and {upper}: {random.randint(lower, upper)}")

    elif choice == 4:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a number between 1 and 4.")
