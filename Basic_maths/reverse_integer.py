n=123
res=0
while n:
    m=n%10
    res=res*10+m
    n//=10
print(res)