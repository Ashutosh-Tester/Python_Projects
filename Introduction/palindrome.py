def palindrome():
    a=int(input("Enter the number : "))
    k=a;s=0;
    while(a!=0):
        r=a%10;
        s=s*10+r;
        a=a//10;
    if(s==k):
        print("Palindrome")
    else:
        print("Not Plaindrome")

palindrome()
palindrome()
palindrome()
    
