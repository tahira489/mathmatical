def factors(num):
    print("the factors of the number are: ")
    for i in range(1, num+1):
        if(num%i==0):
            print(i)

num = int(input("enter any number which you wnat the factors:"))
factors(num)