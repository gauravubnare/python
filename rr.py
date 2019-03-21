a=input("Enter a number")
b=input("Enter a second number")
c= input("Enter the operator")
if(str(c)=='+'):
    d=int(a)+int(b)
    print(str(d))
elif(str(c)=='-'):
    e=int(a)-int(b)
    print(str(e))
elif(str(c)=='*'):
    f=int(a)*int(b)
    print(str(f))
elif(str(c)=='/'):
    g=int(a)/int(b)
    print(int(g))
else:
    print("Invalid Operator selected. Hence cannot perform any operations ")
