num=int(input("enter your number : "))
temp=num
revnum=0
while temp>0:
    digit=temp%10
    revnum=revnum*10+digit
    temp=temp//10
if (revnum==num):
    print(num,"is a palindrome")
else:
    print(num,"is a not palindrome")
