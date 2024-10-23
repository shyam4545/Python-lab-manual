mport msp

def create_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(content)
    except FileNotFoundError:
        print("File '" + filename + "' not found.")

def append_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)

def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
    except FileNotFoundError:
        print("File '" + source + "' not found.")

def main():
    create_file("example.txt", "Hello, this is a sample file.\n")
    read_file("example.txt")
    append_to_file("example.txt", "This line is appended.\n")
    read_file("example.txt")
    copy_file("example.txt", "copy_example.txt")
    read_file("copy_example.txt")

if _name_ == "_main_":
    main()
