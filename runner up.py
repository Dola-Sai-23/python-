# Read the size of the list
n = int(input("Enter the size of the list: "))

# Initialize an empty list
numbers = []

# Read 'n' numbers from the user
print("Enter the numbers:")
for _ in range(n):
    value = int(input())
    numbers.append(value)

# Remove duplicates to ensure uniqueness
unique_numbers = list(set(numbers))

# Check if there's at least two unique numbers
if len(unique_numbers) < 2:
    print("There is no second largest number.")
else:
    # Sort the list in descending order
    unique_numbers.sort(reverse=True)
    # The second element is the second largest
    print("Second largest number:", unique_numbers[1])
