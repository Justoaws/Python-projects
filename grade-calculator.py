# Write a program that will ask a student for their grade in 5 subjects
# Calculate your average grade and print grade from A-E.

grade_A = 90
grade_B = 80
grade_C = 70
grade_D = 60
grade_E = 'Failed'


subjetc1 = 75
subject2 = 10
subject3 = 30
subject4 = 40
subject5 = 20

sum = subjetc1 + subject2 + subject3 + subject4 + subject5
number_subject = 5

average = sum / number_subject

print(sum)
print(f'the average of this student is {average}')

if average > 90 and average != [80, 70, 60]:
    print('PASSED')

elif average < 60 :
    print('FAILLED')



