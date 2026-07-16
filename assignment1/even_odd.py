def generate_even_odd(start,end):

    print(f"Even numbers from {start} to {end}")
    for i in range (start,end +1,2):
        if i%2 == 0:
            print(f"{i}")

    print(f"Odd numbers from {start} to {end}")
    for i in range (start,end +1):
        if i%2 != 0:
            print(f"{i}")

def main():
    start, end = map(int, input().split())

    if start> end:
        start, end = end, start
        
    generate_even_odd(start=start, end=end)

if __name__ == "__main__":
    main()