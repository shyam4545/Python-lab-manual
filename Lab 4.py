numbers = input("Enter a list of numbers (separated by spaces): ")
number_list = numbers.split()

target = input("Enter the number to search for: ")

found = False

for index in range(len(number_list)):
    if number_list[index] == target:
        print(f"Number {target} found at index {index}.")
        found = True
        break

if not found:
    print("Number", target, "not found in the list.")
