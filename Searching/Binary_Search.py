def binary_search(arr,target):
    l=0
    h=len(arr)-1
    while(l<=h):
        mid=(l+h)//2  #finding out the mid element
        if arr[mid]==target:
            return mid+1
        elif arr[mid]<target:
            l=mid+1
        else:
            h=mid-1
    return -1

arr=list(map(int,input().split())) #taking the input array
target=int(input()) #Input of Target from user
res=binary_search(arr,target) #calling the function and storing the result
if res!=-1:
    print("found at index:",res) 
else:
    print("Not Found")