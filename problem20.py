#Write a python program that takes a list of numbers and returns their sum.

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
# Example usage:
if __name__ == "__main__":
    # Example list of numbers
    numbers = [1, 2, 3, 4, 5]
    # Calculate the sum of numbers
    result = calculate_sum(numbers)
    # Print the result
    print(f"The sum of {numbers} is: {result}")
