n=1
while n==1:
    num=int(input("Enter a number:"))
    op=input("Enter which operation:")
    numm=int(input ("Enter another number:"))
    
    if (op=='+'):
        print("The sum is:",num+numm)
    elif (op=='-'):
        print("The difference is:",num-numm)  
    elif (op=='*'):
        print("The multiplication is:",num*numm)    
    elif (op=='/'):
        print("The division is:",num/numm)
    else:
        print("Enter a valid operation")
    n=int(input("Enter 1 to continue or Enter 0 to stop:"))  
    
else:
    print("Feel free to use again!")



    