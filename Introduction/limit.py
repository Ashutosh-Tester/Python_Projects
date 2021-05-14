#Program to find values between 1500 and 2700 which are diisible by 7 and are multiple of 5.
a=int(input("Enter starting limit : "))
b=int(input("Enter ending limit : "))          
for i in range(a,b+1):
    if i%7==0 and i%5==0:
        print(i,end="\n")
