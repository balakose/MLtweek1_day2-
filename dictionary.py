#3
student_dict={
    101:"alice",
    102:"bob",
    103:"charlie"
}
def search_student_name(roll_no):
    name=student_dict.get(roll_no)
    if name:
        print(f"student with roll no {roll_no} is {name}.")
    else:
        print(f"no student found with roll no {roll_no}.")
search_student_name(102)
search_student_name(105)         


