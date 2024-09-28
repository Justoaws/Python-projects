#Write a program that will ask user for a number than check whether 
# that number is EVEN or ODD. 
# number = 9

# if number > 2 and number != [4, 6, 8]:
#     print(f"{number} is an ODD")



number = int(input('please enter a number between 1 and 100\n'))

if number % 2 == 0:
    print(f'{number} is an EVEN')

elif number % 2 == 1:
    print(f'{number} is an ODD')
