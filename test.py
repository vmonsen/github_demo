test = "hello"

print()
print(test)

print('Hello!')

#int('dog')

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#print(thisdict["xxx"])

#geek = "Geeks"
#num = 4
#print(geek + num + geek)

#val = 6 / 0

print("Give me two numbers")
print("Enter 'q' to quit")

while True:
    first_num = input("\nFirst number: ")
    if first_num == 'q':
        break
    second_num = input("Second number: ")
    if second_num == 'q':
        break
    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("You can not divide by 0")
    else:
        print('You get: ', answer)




