import math
def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    sqrt_dis=math.sqrt(discriminant)
    root1 = (-b + sqrt_dis) / (2*a)
    root2 = (-b - sqrt_dis) / (2*a)
    root1=round(root1,2)
    root2=round(root2,2)
    return root1,root2
a=int(input("Enter value for a:"))
b=int(input("Enter value for b:"))
c=int(input("Enter value for c:"))
roots=find_roots(a,b,c)
if roots:
    print("The roots are: ",roots[0]," and ",roots[1])
else:
    print("The quadratic equation has no real roots")