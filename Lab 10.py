def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Please provide numbers.")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: An I/O error occurred.")

def main():
    divide_numbers(10, 2)
    divide_numbers(10, 0)
    divide_numbers(10, 'a')
    read_file('example.txt')
    read_file('non_existent_file.txt')

if _name_ == "_main_":
    main()
