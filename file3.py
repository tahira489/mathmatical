def romantoint(a):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    integer = 0
    for i in range(len(a)):
        if i+1<len(a) and roman [a[i]] < roman [a[i + 1]]:
            integer -= roman[a[i]]
        else:
            integer += roman[a[i]]
    return integer

a = input("enter the roman numeral:")
print("the integer formm of a is:", romantoint(a))