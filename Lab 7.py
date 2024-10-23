def greet(name, message="Hello"):
    print(f"{message}, {name}!")

def add_numbers(*args):
    total = sum(args)
    print(f"The sum is: {total}")

def display_info(name, age, **kwargs):
    info = f"Name: {name}, Age: {age}"
    for key, value in kwargs.items():
        info += f", {key}: {value}"
    print(info)

def main():
    greet("Alice")
    greet("Bob", "Welcome")

    add_numbers(1, 2, 3)
    add_numbers(4, 5, 6, 7, 8)

    display_info("Charlie", 25)
    display_info("David", 30, city="New York")

    display_info("Eve", 28, hobby="painting", job="developer")

if _name_ == "_main_":
    main()
