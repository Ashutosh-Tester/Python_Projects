def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)


a = int(input('Enter First Number: '))
b = int(input('Enter Second Number: '))


print('The GCD of',a,'and',b,'is',gcd(a,b))
