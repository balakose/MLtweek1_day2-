#1
marks=[[85,67,78],[76,87,89],[91,97,87]]
for i in range (3):
    total=sum(marks[i])
    average=total/3
    print(f"student {chr(65+i)}-total:{total},average:{average:.2f}")
    
