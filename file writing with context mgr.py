poem = '''\
There once was a man from Nantucket
Who kept all his stuff in a bucket
...
'''

with open('poem.txt', 'wt') as file_out:
    file_out.write(poem)

# context managers are good equally with reading and writing.
# designed to make your life easier because it handles the file close for you.
