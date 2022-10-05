n=int(input("Enter the number:"))
p=2*n
for i in range(1,p+1):
    if(i<=5):
        for j in range(1,i+1):
            print(j,end=" ")
    elif(i>5):
        for j in range(1,p+2-i):
            print(j,end=" ")
    print()