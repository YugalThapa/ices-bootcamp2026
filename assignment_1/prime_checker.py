def prime_checker(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def main():
    num = int(input("Enter a number: "))
    is_prime = prime_checker(num)

    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")


if __name__ == "__main__":
    main()