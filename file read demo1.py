

DATA_FILE = 'dta.txt'

try:

    file_in = open(DATA_FILE, 'rt')
    sayings = []

    for line in file_in:
        sayings.append(line)

    # print(sayings)

    file_in.close()

    for saying in sayings:
        print(saying, end='')

except FileNotFoundError as e:
    print(f'Error: file "{DATA_FILE}" not found')
    print(e.strerror)

