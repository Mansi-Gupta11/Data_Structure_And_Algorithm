def partition(arr,low,high):
    i=low-1
    pivot=arr[high] #initializing last index as pivot element
    for j in range(low,high):
        if arr[j]<=pivot: #as long as element is smaller than pivot they will be swapped
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1] # means no element smaller than pivot left 
    return i+1


def quick_sort(arr,low,high):
    if low<high:
        pivot=partition(arr,low,high) #finding the poit for divide and conquer
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)


arr=list(map(int,input().split()))
n=len(arr)
quick_sort(arr,0,n-1)
print(arr)
