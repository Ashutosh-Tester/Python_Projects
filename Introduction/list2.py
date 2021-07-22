"""list1=['hello','how','are','you']
list2=['i','am','fine']
print(list1)
print(len(list1))
for i in list1:
    print(i,end=" ")
print()
for j in list2:
    print(j,end=" ")
list1.append("Neelay")
list2.append("Neelesh")
list1.insert(5,"xyz")
print(list1)
list1.extend(list2)
print(list1)
print(list1," ",list2)"""
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

    




