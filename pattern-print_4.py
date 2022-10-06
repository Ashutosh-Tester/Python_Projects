x=(int)(input())
a=x
while(1):
    if a==0:
        break
    for i in range(1,x+1):
        
        for j in range(1,i+1):
            print (j,end=" ")
        
        print()
        
    for i in range(x,0,-1):
        
        for j in range(1,i+1):
            print (j,end=" ")
            # j=j-1
        # i=i-1
        a=a-1
        print()
    a=0