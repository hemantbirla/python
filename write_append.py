#Write in file
file = open('output.txt', 'w')
print('Enter text to write to the file: ')
s = input()
writing_file = file.write(s+'\n')
if writing_file:
    print('Data successfully written to output.txt.')
file.close()

#append in file
file1 = open('output.txt', 'a')
print('Enter additional text to append: ')
a = input()
append_file = file1.write(a)
if append_file:
    print('Data successfully appended.')
file1.close()

#read file
file2 = open('output.txt', 'r')
reading_file = file2.read()
print('Final content of output.txt:')
print(reading_file)
file2.close()