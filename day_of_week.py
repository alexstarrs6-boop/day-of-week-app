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

# Tell the user whether it's a weekday or the weekend.
if day_number == 6 or day_number == 7:
    print('It is the weekend!')
elif day_number >= 1 and day_number <= 5:
    print('It is a weekday.')
