try:
    file = open('sample.txt', 'r')
    print('Reading File content:')
    print(file.read())
    file.close()
except:
    print('Error: The file \'sample.txt\' was not found.')