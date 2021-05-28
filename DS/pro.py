a = int(input("Enter a number: "))
i=int(2)
for i in range(2,i*i):
    if(int(a%i)==0):
        print("Not prime")
        break
    else:
        print("prime")
        break
