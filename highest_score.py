student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)


max = 0
for items in student_scores:
  if items > max:
    max = items
print(f"The highest score in the class is: {max}")
