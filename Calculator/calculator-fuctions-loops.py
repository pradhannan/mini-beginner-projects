def sum(a,b):
    print(a,"+",b,"=",a+b)
def diff(a,b):
    print(a,"-",b,"=",a-b)
def mul(a,b):
    print(a,"*",b,"=",a*b)
def div(a,b):
    print(a,"/",b,"=",a/b)


n='y'
while n.lower() == 'y':
    num=int(input("Enter a number:"))
    op=input("Enter which operation:")
    
    
    if (op=='+'):
        numm=int(input ("Enter another number:"))
        sum(num,numm)
    elif (op=='-'):
        numm=int(input ("Enter another number:"))
        diff(num,numm) 
    elif (op=='*'):
        numm=int(input ("Enter another number:"))
        mul(num,numm)   
    elif (op=='/'):
        numm=int(input ("Enter another number:"))
        div(num,numm) 
    else:
        print("Enter a valid operation")
    n=input("Input 'y'or 'Y' to continue")
    
else:
    print("Feel free to use again!")