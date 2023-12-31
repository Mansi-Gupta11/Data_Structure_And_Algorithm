''' One by one rotation 
arr=[1,2,3,4,5,6,7]
d=2
temp=arr[0]
c=0
while(c<d):
    for i in range(len(arr)-1):
        arr[i]=arr[i+1]
    arr[len(arr)-1]=temp
    c+=1
    print(arr)
    
    
Complexity :
Time : O(d*n) --> 
1.The while loop runs for d iterations.
2.Within the while loop, the for loop runs len(arr) - 1 times in each iteration.
3.the overall time complexity of the code can be expressed as O(d * (len(arr) - 1)).

Space: O(1)
  
'''
    
'''Juggling Algorithm'''
def left_rotation(arr, d, n):
    d = d % n
    g_c_d = gcd(d, n)
    for i in range(g_c_d):

        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
 
 

arr=[1,2,3,4,5,6,7]
d=3
n=len(arr)
left_rotation(arr,d,n)
print(arr)