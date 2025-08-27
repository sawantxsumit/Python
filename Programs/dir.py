import os

# this is a program to list all the files inside a directory
# specify the directory path below
directory_path = '/users'

contents = os.listdir(directory_path)

for item in contents:
    print(item)
    