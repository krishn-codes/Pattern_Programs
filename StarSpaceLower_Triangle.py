n = int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(1,n+1-i+1):
        if (j==1) or (j==n+1-i):
            print("*", end =" ")
        else:
            print("_",end = " ")    
    print()            
