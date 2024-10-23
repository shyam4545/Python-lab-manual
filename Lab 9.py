with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")

with open('example.txt', 'r') as file:
    content = file.read()
    print("File content:", content)

with open('example.txt', "a") as file:
    file.write("Appending this line.\n")

with open("example.txt', 'r') as source:
    with open("copy.txt', 'w') as destination:
        destination.write(source.read())
