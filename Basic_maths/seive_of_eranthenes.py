n=10
#n=int(input()) -- For taking users input
res=[0]*(n+1)
i=2
res[0]=1  # Prime starts from 2 so in 0th and 1st index we will insert 1 so it doesnt count these both as prime.
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
