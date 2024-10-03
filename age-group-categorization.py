# Write a program that will prompt the user to enter an interger
# Based on the input, cqtegorize the person into one of the following life stages :

# age = int(input('enter a number between 0 and 150\n'))
# Infant =  0 and 1
# Toddler = 2 and 3
# Child = 4 and 12
# Teenager = 13 and 19
# Adult = 20 and 64
# Senior = 65 and 150


age = int(input('enter a number between 0 and 150\n'))

if age >= 0 and age <= 1:
    print('INFANT')

elif age >= 2 and age <= 3:
    print('TODDLER')

elif age >= 4 and age <= 12:
    print('CHILD')

elif age >= 13 and age <= 19:
    print('TEENAGER')

elif age >= 20 and age <= 64:
    print('ADULT')

elif age >= 65 and age <= 150:
    print('SENIOR')

else:
    print('INVALID AGE')

