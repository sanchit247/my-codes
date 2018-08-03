def heapify(data, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
 
    # Compare left child and root
    if l < n and data[i] < data[l]:
        largest = l
 
    # Compare right child and root
    if r < n and data[largest] < data[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        data[i],data[largest] = data[largest],data[i]
 
        # Heapify the root
        heapify(data, n, largest)
 
# The main function to sort an data array of given size
def heapSort(data):
    n = len(data)
 
    # Build a maxheap
    for i in range(n, -1, -1):
        heapify(data, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)
  
  
numList = [5,8,1,6,3,7,2,4,9]
print('Before sort:')
print(numList)
# Calling 'heapSort' function by passing number data array
heapSort(numList)
print('After sort:')
print(numList)
