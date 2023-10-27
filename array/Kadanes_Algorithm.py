'''Kadane's Algorithm'''
nums = [-2,1,-3,4,-1,2,1,-5,4]
sumi=0
m=float('-inf')
for i in nums:
    sumi+=i
    if sumi<0:
        sumi=0
    m=max(m,sumi)
print(m)
