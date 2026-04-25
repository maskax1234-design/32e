Students ={
    1:"Ahmed ",
    2:"Jama",
    'ID':"Welcome",
    3:56,
    False:True
}
print(Students)

Students[4]="ismail"
print(Students)
Students[2]="Mohamed"
print(Students)

del Students[False]

value =Students.pop(3)
print("Removed value: ", value)
print(Students)
