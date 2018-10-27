# QuickSorting Algorithm

<p align="center">
  <img width="500" height="350" src="http://2.bp.blogspot.com/-6YYLhmuFUoU/Ua6ZU7rsZFI/AAAAAAAAA0s/e8V4fl9UbP4/s1600/quick_sort.jpg">
</p>

---
* Select a pivot => pivot = list_1[0]
* Create left_array left[1:] if (i < pivot) -> quicksort(left_array) until <-> (start_returning) len(base_case) == 1   
* Create right_array left[1:] if i > pivot -> same above
* After Base_Case => return left_array + [pivot] + right_array
---
```python
def quicksort(list_1):
    if len(list_1) < 2:
        return list_1
    else:
        pivot = list_1[0]
        left = [i for i in list_1[1:] if i < pivot]
        right = [i for i in list_1[1:] if i > pivot]
        return quicksort (left) + [pivot] + quicksort(right)
		

print (quicksort([1, 3, 4, 9, 2, 5]))
```
