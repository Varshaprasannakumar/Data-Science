n=int(input("Enter the limit:"))
a=0
b=1
fib=1
print(a)
print(b)
print(fib)
for i in range(2,n):
    temp=b
    b=fib
    fib=temp+b
    print(fib)
