import math
n=int(input())
m=int(input())
g=math.gcd(n,m)
if(n!=0) or (m!=0):
    print(g)
else:
    print("-1")
