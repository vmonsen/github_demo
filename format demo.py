# from math import pi
#
# radius = input('Enter the radius of a circle: ')
#
# area = pi * float(radius) ** 2
#
# print('The area of a circle with radius ' + radius + ' = ' + str(round(area, 2)))
#
# print('The area of a circle with radius {} = {:.2f}'.format(radius, area))
#
# print(f'The area of a circle with radius {radius} = {area:.2f}')

guest_1 = 'Eric'
guest_2 = 'Dan'
host = 'Mary'

# welcome_message = f"We would like to welcome {guest_1}" \
#                  f"and {guest_2} to {host}'s party"


welcome_message = f"We would like to welcome {guest_1:^10s} and {guest_2:>10s} to {host}'s party"

print(welcome_message)






