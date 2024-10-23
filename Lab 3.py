def is_prime(num):
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

while True:
  print("\nOptions:")
  print("1. Add two numbers")
  print("2. Check If a number is prime")
  print("3. Exit")

  choice = input("Choose an option (1-3): ")

  if choice == "1":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

  elif choice == "2":
    num = int(input("Enter a number to check if it's prime: "))
    if is_prime(num):
      print(f"{num} is a prime number.")
    else:
      print(f"{num} is not a prime number.")

  elif choice == "3":
    print("Exiting the program.")
    break

  else:
    print("Invalid choice. Please select 1, 2, or 3.")
