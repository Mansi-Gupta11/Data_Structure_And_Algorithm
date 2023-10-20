n=10
res=[0]*(n+1)
i=2
res[0]=1
res[1]=1
ans=[]
while(i*i<=n):
    if res[i]==0:
        for j in range(i*i,n+1,i):
            res[j]=1
    i+=1
print(res)
for i in range(2,n+1):
    if  res[i]==0:
        ans.append(i)
print(ans)