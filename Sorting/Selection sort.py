def selection_sort(arr):
    for i in range(len(arr)):
        min=i #initializing the minimum element
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]: #comparing if anyother element is smaller than the minimum element from i+1 index 
                min=j  #updating the minimum element
        arr[i],arr[min]=arr[min],arr[i] #swapping 
                
arr=list(map(int,input().split())) # taking input of the array
selection_sort(arr) #function calling
print(arr)
