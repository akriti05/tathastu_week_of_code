n=int(input("enter the number:"))
#even odd

if n%2==0:
    print("the number is even:",n)
else:
    print("the number is odd")

#prime no.
if n>1:
    for i in range(2,n):  #for checking the factor
        if(n%i)==0:
            print(n,"not prime")
            break
    else:
        print(n, "is prime")

else:
    print(n,"not prime")

#palindrome

temp=n
r=0
while(n>0):
    d=n%10
    r=r*10+d
    n=n//10
if(temp==r):
    print("palindrome no.")
else:
    print(" not palindrome no.")

#armstrong no.

s=0
t=n
while t>0:
    d=t%10
    s=s+ d**3
    t=t//10
if n==s:
    print("armstrong no.")
else:
    print("not armstrong no.")

