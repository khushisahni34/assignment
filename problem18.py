'''Write a python program that checks if two strings are anagrams of each
other.'''


def are_anagrams_method1(str1, str2):
    # Method 1: Using sorted characters
    # Convert strings to lists of characters, sort them, and compare
    return sorted(str1) == sorted(str2)


def are_anagrams_method2(str1, str2):
    # Method 2: Using character frequency counting
    # Count frequencies of characters in both strings and compare
    if len(str1) != len(str2):
        return False

    # Create dictionaries to store character frequencies
    freq1 = {}
    freq2 = {}

    # Count frequencies in str1
    for char in str1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1

    # Count frequencies in str2
    for char in str2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1

    # Compare frequency dictionaries
    return freq1 == freq2


# Example usage:
if __name__ == "__main__":
    string1 = "listen"
    string2 = "silent"

    # Method 1: Using sorted characters
    if are_anagrams_method1(string1, string2):
        print(f"'{string1}' and '{string2}' are anagrams (Method 1)")
    else:
        print(f"'{string1}' and '{string2}' are not anagrams (Method 1)")

    # Method 2: Using character frequency counting
    if are_anagrams_method2(string1, string2):
        print(f"'{string1}' and '{string2}' are anagrams (Method 2)")
    else:
        print(f"'{string1}' and '{string2}' are not anagrams (Method 2)")