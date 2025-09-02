N= int (input("Enter a Number: "))
for i in range (N+1):
    for j in range (1,N-i):
        print(j, end= " ")
    print()