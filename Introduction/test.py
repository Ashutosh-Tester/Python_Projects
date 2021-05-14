""" Program to find numbers between 1500 and 2700 which are divisible 
by 7 and multiple of 5"""
# for i in range(1500,2701):
 # if i%5==0 and i%7==0:
  # print(i)  
"""Program to convert celsius to fahrenheit and vice versa."""
print("Enter 1 to convert celsius to fahreheit")
print("Enter 2 to convert fahrenheit to celsius")
print("Enter your choice :")
ch=int(input())
if ch==1:
    # print("Enter the temperature in celsius : ")
    cel=int(input("Enter the temperature in celsius : "))
    cel=round(((9*cel)+160)/5,0)
    print("The temperature is : ",cel,end=" F")
elif ch==2:
    # print("Enter the temperature in fahrenheit : ")
    fah=int(input("Enter the temperature in fahrenheit : "))
    fah=round(((5*fah)-160)/9,0)
    print("The temperature is : ",fah,end=" C")
else :
     print("Enter correct choice : ")
    
