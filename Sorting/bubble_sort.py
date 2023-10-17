def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]: #checking with the adjacent elements
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
                
#driver's code for testing the code
arr=list(map(int,input().split()))
bubble_sort(arr)
print(arr)