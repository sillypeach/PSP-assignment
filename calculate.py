from Linklist import LinkedList
def input_from_keyboard():
    input_string = input("input your number：")
    number_list = input_string.split()
    return map(float, number_list)
def input_from_file(file_path):
    with open(file_path, 'r') as file:
        number_list = file.read().split()
    return map(float, number_list)
def fill_linked_list(numbers):
    linked_list = LinkedList()
    for number in numbers:
        linked_list.append(number)
    return linked_list
def main():
    choice = input("（1-keyboard，2-file）：")
    if choice == '1':
        numbers = input_from_keyboard()
    elif choice == '2':
        file_path = input("file_path：")
        numbers = input_from_file(file_path)
    else:
        print("Invalid input")
        return
    ll = fill_linked_list(numbers)
    ll.print_list()
    print("average：", ll.mean())
    print("deviation：", ll.standard_deviation())
if __name__ == "__main__":
    main()

