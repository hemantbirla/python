file = open('sample.txt', 'r')
if file:
    reading_file1 = file.readline()
    reading_file2 = file.readline()
    print('Reading file content:')
    print('Line1: ',reading_file1)
    print('Line2: ',reading_file2)

else:
    print('Error: The file \'sample.txt\' was not found')

file.close()