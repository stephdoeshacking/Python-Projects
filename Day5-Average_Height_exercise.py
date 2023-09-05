# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# print(student_heights)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# replicating sum() function
total_height = 0
for height in student_heights:
  total_height = total_height + height # can use += as well
# print(total_height)

# replicating len() function
number_of_students = 0
for student in student_heights:
  number_of_students += 1 # runs the for loops for how many entries there are in the list
# print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)

### easy way:
# total_height = sum(student_heights)
# number_of_students = len(student_heights)
# average_height = round(total_height / number_of_students)
# print(average_height)



# 156 178 165 171 187
