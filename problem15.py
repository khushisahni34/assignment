# Write a program that reads data from a CSV file and prints it to the
# console
import csv
def read_csv_file(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"Error: {e}")
# Example usage:
if __name__ == "__main__":
    filename = 'data.csv'  # Replace with your CSV file name
    # Call the function to read and print the CSV file contents
    read_csv_file(filename)