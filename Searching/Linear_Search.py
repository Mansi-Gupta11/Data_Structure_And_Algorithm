def linear_search(arr,target):
    n=len(arr)
    for i in range(n):
        if arr[i]==target:
            return i # Return the index where the target element is found
    return -1 
arr=list(map(int,input().split())) #taking the input array
target=int(input()) #Input of Target from user
res=linear_search(arr,target) #calling the function and storing the result
if res!=-1:
    print("found at index:",res) 
else:
    print("Not Found")