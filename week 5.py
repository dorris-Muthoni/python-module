# file.py

def create_file():
    try:
        # Create and write to the file
        with open('my_file.txt', 'w') as file:
            file.write("This is the first line of text.\n")
            file.write("The second line contains the number: 42\n")
            file.write("Here is another line with some more text.\n")
        print("File 'my_file.txt' created and data written successfully.")
    
    except PermissionError:
        print("Error: Permission denied when trying to write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def read_file():
    try:
        # Read and display the contents of the file
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("\nContents of 'my_file.txt':")
            print(content)

    except FileNotFoundError:
        print("Error: The file 'my_file.txt' was not found.")
    except PermissionError:
        print("Error: Permission denied when trying to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def append_to_file():
    try:
        # Append additional lines to the file
        with open('my_file.txt', 'a') as file:
            file.write("This line is appended to the file.\n")
            file.write("Appending the number: 99\n")
            file.write("Finally, this is the last appended line.\n")
        print("Additional lines appended to 'my_file.txt' successfully.")
    
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' was not found.")
    except PermissionError:
        print("Error: Permission denied when trying to append to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read the file again to display updated contents
