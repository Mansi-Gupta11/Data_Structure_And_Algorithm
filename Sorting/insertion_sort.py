def insertion_sort(arr):
    # Start iterating through the array from the second element (index 1)
    for i in range(1,len(arr)):
        key=arr[i] # Select the current element as the key to be inserted
        j=i-1
        # Move elements of arr[0..i-1] that are greater than key to one position ahead
        while(j>=0 and key< arr[j]):
            arr[j+1]=arr[j]
            j-=1 # Move to the previous element
        arr[j+1]=key
                
    
arr=list(map(int,input().split()))
insertion_sort(arr)
print(arr)
