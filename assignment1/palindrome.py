def palindrome_checker(data):
    if isinstance(data, int):
        actual_data = data
        reverse_data = 0

        while data > 0:
            digit = data % 10
            reverse_data = reverse_data * 10 + digit
            data //= 10

        return actual_data == reverse_data

    elif isinstance(data, str):
        data = data.lower()
        return data == data[::-1]


def main():
    data = input("Enter here: ")

    if data.isdigit():
        data = int(data)

    if palindrome_checker(data):
        print(f"{data} is palindrome")
    else:
        print(f"{data} is not palindrome")


if __name__ == "__main__":
    main()