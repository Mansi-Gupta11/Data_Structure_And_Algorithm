def binary_sort_optimized(arr):
    for i in range(len(arr)):
        swapped=False
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True #As you iterate through the array and compare adjacent elements, if a swap is made, you set swapped to True. This indicates that at least one swap occurred during this pass.
        if swapped==False: #After completing a full pass through the array, you check the value of swapped. If it's still False, it means that no swaps were made during the entire pass, which indicates that the array is already sorted
            break
    
arr=list(map(int,input().split()))
binary_sort_optimized(arr)
print(arr)
