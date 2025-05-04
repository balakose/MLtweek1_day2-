#2
students=[
    (101,"alice",18),
    (102,"bob",19),
    (103,"chalie",18)
]
print("Student Information: ")
print("----------------")
for student in students:
    roll_no,name,age=student
    print(f"roll no:{roll_no}")
    print (f"name  :{name}")
    print(f"age  :{age}")
    print("--------------------------")
