Students =['Ahmed','Jama','Mohamed', 'omar']

# Return all students 
print("Student list:  " , Students)
# Select specific index
print("student one" , Students[1])
# Add new student in the list
Students.append("Fadumo")
#Return all students refreshment
print(Students)
# Remove using value
Students.remove('omar')
# Remove using Index
remove_student=Students.pop(2)
print("Removed student",remove_student)

# Represent list using witha loop

for student in Students:
    print(student)
