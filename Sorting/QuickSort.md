# Quick Sort

<p align="center">
  <img width="500" height="350" src="http://2.bp.blogspot.com/-6YYLhmuFUoU/Ua6ZU7rsZFI/AAAAAAAAA0s/e8V4fl9UbP4/s1600/quick_sort.jpg">
</p>

---
**Divide and Conquer**
* Select a pivot => pivot = list_1[0]
* Create left_array left[1:] if (i < pivot) -> quicksort(left_array) until <-> (start_returning) len(base_case) == 1   
* Create right_array left[1:] if i > pivot -> same above
* After Base_Case => return left_array + [pivot] + right_array
---
**Time Conplexity**
1. If quick_sort uses 1st element as pivot (worst)
	* Will take at most O(n) recursion call stacks before the first recursion returns
2. If quick_sort uses median element as pivot (average)
    * Take at most O(log n) call stacks before the first recursion returns 
3. Each level of stack: Do task O(n) time
4. Take around **O(n logn)** if use with random point
5. Faster than **mergesort()** 
    * Is in-place (MergeSort requires extra memory linear to number of elements to be sorted).
    * Has a small hidden constant.
---
**QuickSort.py**
```python
from random import randint

def quicksort(list_1):
    if len(list_1) < 2:
        return list_1  
    else:
        # Choose the random point
        rand_pt = randint(0, len(list_1))
        pivot = list_1[rand_pt]
        # Modified the list_1 to exclude the pivot
        list_1 = list_1[0:rand_pt] + list_1[rand_pt+1:]
        # Left and right arrays 
        left = [i for i in list_1 if i < pivot]
        right = [i for i in list_1 if i > pivot]
        # Check that a value == pivot is also counted
        mid_array = [i for i in list_1 if i == pivot]
		
        return quicksort (left) + [pivot] + mid_array + quicksort(right)
		

print (quicksort([1, 3, 4, 9, 2, 3, 5]))
```
