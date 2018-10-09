# MERGE SORT

<p align="center">
  <img width="500" height="350" src="https://dobicode.files.wordpress.com/2018/09/merge-sort.png">
</p

* Merge 2 arrays left and right at each level (Used at all nodes and levels)
* **Use 2 pointers to iterate over two lists**
```python 
def merge(left, right):
    result = []
    i,j = 0,0
    # 2 pointers
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # if there are still items left on the left
    while (i < len(left)):
        result.append(left[i])
        i += 1
    # if there are still items left on the right
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result
```
* **Divide and Merge**
```python 
def merge_sort(L):
    print('merge sort: ' + str(L))
    # Base Case
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        '''
        This recursion will start
        returning base case when len(L) == 1 or 0
        '''
        # Start when len(L) = 1
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)
```
