# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# replicate the max() function
high_score = 0
for score in student_scores:
  if score > high_score: #this runs through the loop checking every entry to see which score will be the highest
    high_score = score # single = assigns

print(f"The highest score in the class is: {high_score}")

### easy way ###
# min()
# print(max(student_scores))
