'''Write a python program that removes all punctuation from a given string.'''
import string
def remove_punctuation(input_string):
    # Create a translation table that maps each punctuation character to None
    translator = str.maketrans('', '', string.punctuation)

    # Use the translation table to remove punctuation characters
    return input_string.translate(translator)
# Example usage:
if __name__ == "__main__":
    input_string = "Hello, world! This is a test string with punctuation."
    result = remove_punctuation(input_string)
    print("Original string:", input_string)
    print("String without punctuation:", result)
