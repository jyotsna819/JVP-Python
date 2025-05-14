def print_pattern(rows):
    # Calculate the highest odd number to start with
    total_numbers = sum(range(1, rows * 2, 2))  # Number of odd numbers needed
    max_odd = total_numbers * 2 - 1

    current = max_odd

    for i in range(rows):
        # Print leading spaces
        print("   " * i, end="")

        # Print numbers in row
        count = rows * 2 - 1 - i * 2
        for j in range(count):
            print(f"{current}", end=" ")
            current -= 2
        print()

# Get user input
rows = int(input("Enter number of rows: "))
print_pattern(rows)
