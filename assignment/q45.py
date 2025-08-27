source_path='file1.txt'
destination_path='file2.txt'
with open(source_path, 'r') as src:
        content = src.read()

with open(destination_path, 'w') as dest:
    dest.write(content)

print(f"Content copied from '{source_path}' to '{destination_path}' successfully.")

