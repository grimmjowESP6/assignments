file = open('output.txt', 'w')
txt_w = input('Enter text to write to the file: ')
file.write(txt_w)
file.close()
print('Data successfully written to output.txt.')
print()
file = open('output.txt', 'a')
txt_a = input('Enter additional text to append: ')
file.write('\n'+txt_a)
file.close()
print('Data successfully appended.')
print()
file = open('output.txt', 'r')
print('Final content of output.txt:')
print(file.read())
file.close()
    