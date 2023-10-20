def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  #left child
    r = 2 * i + 2  #right child
 

    if l < n and arr[i] < arr[l]: #checking for the largest element
        largest = l

 
    if r < n and arr[largest] < arr[r]: #checking for the largest element
        largest = r
 
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
 
        heapify(arr, n, largest)
 
def heapSort(arr):
    n = len(arr)
 
    # Build a maxheap
 
    for i in range(n // 2 - 1, -1, -1): #starting from level above the leaf node to build heap
        heapify(arr, n, i)
 
    # extract elements
 
    for i in range(n - 1, 0, -1): #sorting starts
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)
 
 
# Driver code to test above
 
arr = [12, 11, 13, 5, 6, 7, ]
heapSort(arr)
n = len(arr)
