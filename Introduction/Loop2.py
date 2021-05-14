limit=int(input("enter limit : "))
for i in range(0,limit+1,1):
    for j in range(0,i,1):
        print("*",end="")
    print()
for i in range(limit-1,0,-1):
    for j in range(0,i,1):
        print("*",end="")
    print()    
    
