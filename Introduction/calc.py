def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def divide(x,y):
    return x/y
print("Enter 1 -> addition\nEnter 2 -> subtraction\nEnter 3 -> multiply\nEnter 4 -> divide")
ch=int(input("Enter your choice : "))
if(ch==1 or ch==2 or ch==3 or ch==4):
    num1=int(input("Enter first number : "))
    num2=int(input("Enter second number : "))
    if(ch==1):
        print("The sum is : ",addition(num1,num2))
    elif(ch==2):
        print("The result is : ",subtraction(num1,num2))
    elif(ch==3):
        print("The product is : ",multiplication(num1,num2))
    elif(ch==4):
        print("The quotient is : ",divide(num1,num2))
else:
    print("Invalid Choice")
    
    
    



