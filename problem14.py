# Write a program that reads multiple lines of input from the user until they
# enter an empty line, then prints all the lines.
def read_lines_until_empty():
    lines = []
    while True:
        line = input("Enter a line (or press Enter to finish): ")
        if line.strip() == "":
            break
        lines.append(line)
    if lines:
        print("\nLines entered:")
        for line in lines:
            print(line)
    else:
        print("No lines were entered.")
if __name__ == "__main__":
    read_lines_until_empty()
