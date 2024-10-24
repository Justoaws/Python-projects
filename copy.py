# Write a function called "copy" which takes in a file name and a "new file name" 
# and copies the contents of the first file into the second file.

def copy_content():
    with open ('copy.txt', 'w') as file:
        file.write('house\n')
        file.write('cars\n')
        file.write('clothes\n')
        file.write('tv')
    
    new_file_name = []
    with open('copy.txt', 'r') as file:
       for line in file:
            new_file_name.append(line.strip())
    print(new_file_name)

copy_content()
