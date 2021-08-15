num=int(input("enter your number:"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,"is not a prime number")
            print(i ,"*",num//i,"=",num)
            break
    else:
        print(num,"is a prime number")
else:
        print(num,"is a prime number")