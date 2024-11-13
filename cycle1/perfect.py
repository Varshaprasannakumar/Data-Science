def is_perfect(num):
    sum = 0
    for i in range(1,num):
        if num%i == 0:
            sum=sum+i
    return sum == num


n=int(input("Enter a number:"))
if is_perfect(n):
    print(n," is a perfect number.")
else:
    print(n," is not a perfect number.")

