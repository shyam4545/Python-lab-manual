def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def main():
    strings = input("Enter a sorted list of strings (separated by spaces): ")
    string_list = strings.split()
    target = input("Enter the string to search for: ")

    result = binary_search(string_list, target)

    if result != -1:
        print("String '{}' found at index {}".format(target, result))
    else:
        print("String '{}' not found in the list.".format(target))

if _name_ == "_main_":
    main()
