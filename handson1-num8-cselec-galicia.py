def write_to_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
            print(f"Content written to {file_name} successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def read_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content read from {file_name}:\n{content}")
    except FileNotFoundError:
        print(f"Error: File {file_name} not found.")
    except Exception as e:
        print(f"Error reading from file: {e}")

file_name = "example_file.txt"
content_to_write = "Hello, this is a sample content that will be written to the file."

write_to_file(file_name, content_to_write)


read_from_file(file_name)
