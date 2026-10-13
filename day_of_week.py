# Day of the Week
# This program asks the user for a number from 1 through 7
# and displays the corresponding day of the week.

# Get a number from the user.
day_number = int(input('Enter a number (1-7): '))

# Determine the day of the week using an if-elif-else statement.
if day_number == 1:
    print('Monday')
elif day_number == 2:
    print('Tuesday')
elif day_number == 3:
    print('Wednesday')
elif day_number == 4:
    print('Thursday')
elif day_number == 5:
    print('Friday')
elif day_number == 6:
    print('Saturday')
elif day_number == 7:
    print('Sunday')
else:
    print('Error: Please enter a number in the range of 1 through 7.')
