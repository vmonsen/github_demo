message_1 = 'The rain in Spain falls mainly on the plain\n'

message_2 = 'No one expected the Spanish Inquisition\n'

# Create a file handle for writing to a text file.
# Open the file in write mode
file_out = open('data.txt', 'wt')

#file_out.write(message_1)
#file_out.write(message_2)

print(message_1, message_2, file=file_out, sep='', end='')

print(message_1, message_2, file=file_out, sep='')

print('test')
print('this')

# Close the file handle
# Good cleanup practice

file_out.close()



