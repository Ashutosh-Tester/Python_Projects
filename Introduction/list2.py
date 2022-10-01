
size=int(input("Enter the size of first array : "))
A=[]
print("Enter values")
for i in range(size):
    #a=int(input())
    A.append(input())
for i in A:
    print(i,end=" ")
B=[]
size2=int(input("\nEnter size of second array : "))
print("Enter values")
for i in range(size2):
    B.append(input())
for j in B:
    print(j,end=" ")
if size>size2:
    print()
    C=[]
    C.append(int(A+B))
    #for i in range(0,size2):
    for i in C:
        print(i,end=" ")
else:
    print("Size are not equal",end="")

    




