#Write a program that will ask user for a number than check whether 
# that number is EVEN or ODD. 
# number = 9



number = int(input('please enter a number between 1 and 100\n'))

if number % 2 == 0:
    print(f'{number} is an EVEN')

else:
    print(f'{number} is an ODD')
