# Selection sort
---
1. Assume that the leftmost element is sorted
2. Iterate over n - 1 remaining items to find the ***smaller** if any
3. Add the **smallest** into the new array 
4. Repeat 1 - 3 until there is 0 remaining items to compare 
---
* **SelectionSort.py**
```python 
def findthesmallest(arr):
    # suppose that the left list is sorted
    smallest = arr[0]
    smallest_index = 0
    
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
	
    return smallest_index

def selectionsort(arr):
    new_arr = []
    # For each i+= 1, n-=1 
    for i in range (len(arr)):
        smallest_index = findthesmallest(arr)
        new_arr.append(arr.pop(smallest_index))

    return new_arr

print (selectionsort([5, 3, 4, 8, 10]))
```
