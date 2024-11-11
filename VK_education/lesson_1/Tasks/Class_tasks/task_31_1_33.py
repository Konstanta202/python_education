import os
def write_and_read(text):

    file_name = 'file_test'
    my_file = open(file_name, 'w').write(text)
    with open(my_file, 'r') as file:
        file_data = file.readline()
        file.close()
    return file_data

text = input()
print(write_and_read(text))
