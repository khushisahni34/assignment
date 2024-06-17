# problem =Write a program in python that counts the frequency of each character in a string.
def count_frequency(input_string):
    # Initialize an empty dictionary to store the frequency of each character
    frequency = {}
    # Iterate through each character in the input string
    for char in input_string:
        if char in frequency:
            # If the character is already in the dictionary, increment its count
            frequency[char] += 1
        else:
            # If the character is not in the dictionary, add it with a count of 1
            frequency[char] = 1
    return frequency
if __name__ == "__main__":
    input_string = "Hello, World!"
    frequency = count_frequency(input_string)

    # Print the frequency of each character
    for char, count in frequency.items():
        print(f"Character '{char}' occurs {count} times")