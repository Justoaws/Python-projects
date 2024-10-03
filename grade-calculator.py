# Write a program that will ask a student for their grade in 5 subjects
# Calculate your average grade and print grade from A-E.

subject1 = int(input('enter the grade of that french:\n'))
subject2 = int(input('enter the grade of that maths:\n'))
subject3 = int(input('enter the grade of that economics:\n'))
subject4 = int(input('enter the grade of that sciences:\n'))
subject5 = int(input('enter the grade of that english:\n'))

number_subject = 5

average = subject1 + subject2 + subject3 + subject4 + subject5 / number_subject

if average >= 90:
    print('you PASSED with A')

elif average >= 80 and average <= 70:
    print('you PASSED with B')

elif average >= 70 and average <= 60:
    print('you PASSED with C')

else:
    print('you FAILLED')




