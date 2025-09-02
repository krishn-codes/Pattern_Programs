N= int (input("Enter a Number: "))
num=1
for i in range (1,N):
    for j in range (i):
        print(num, end= " ")
        num=num+1
    print()