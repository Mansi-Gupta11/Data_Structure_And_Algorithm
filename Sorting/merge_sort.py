def merge(arr):
    if len(arr)>1:# If the list has more than one element, continue
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        merge(left) # Recursively sort the left sublist
        merge(right)  # Recursively sort the right sublist
        
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i<len(left):  
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
        
        

arr=list(map(int,input().split()))
n=len(arr)
merge(arr)
print(arr)

'''
Time Complexity : O(n * logn)
1.The algorithm recursively divides the input list into two halves until each sublist contains only one element. This division is done in O(log n) time
2. he merge step combines two sorted sublists into a single sorted list. This step is performed at every level of recursion. The time complexity of the merge step is O(n), where 'n' is the total number of elements in the input list
'''
