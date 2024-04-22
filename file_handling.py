# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("First line\n")
        file.write("Second line with number: 42\n")
        file.write("Third line with a float: 3.14\n")
except Exception as e:
    print(f"Error during file creation: {e}")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("File contents:")
        print(file.read())
except Exception as e:
    print(f"Error during file reading: {e}")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Fourth line\n")
        file.write("Fifth line with a date: 2023-03-15\n")
        file.write("Sixth line with a boolean: True\n")
except Exception as e:
    print(f"Error during file appending: {e}")

# Error Handling
try:
    with open("my_file.txt", "r") as file:
        print("File contents:")
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    print("File handling complete.")