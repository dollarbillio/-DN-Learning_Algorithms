# Binary Search
---
* Time Complexity: <img src="https://latex.codecogs.com/gif.latex?O%28log_n%29" />
---
* **BinarySearch.py**
```python
def binarySearch(list_1, item):
    low = 0
    high = len(list_1) - 1

    while low <= high:
        mid = (low + high) // 2
        if list_1[mid] == item:
            return "There Found"
        elif list_1[mid] > item:
            high = mid - 1
        elif list_1[mid] < item:
            low = mid + 1
	
    return "There is nothing here"

print (binarySearch([1, 2, 3, 4], 1))
```
---
* **BinarySearch.java**
```java
public class BinarySearch {

    // Method attribute
    private static String binarySearch(int[] list, int item) {
        int low = 0;
        int high = list.length - 1;

        while (low <= high) {
            int mid = (low + high) / 2;
            if (list[mid] == item) {
                return "Found in position " + Integer.toString(mid);
            } else if (list[mid] < item) {
                low = mid + 1;
            } else if (list[mid] > item) {
                high = mid - 1;
            }
        }
        return "Not found in any positions";
    }

    // Main method
    public static void main(String[] args) {
        int[] myList = { 1, 2, 3, 4 };
        System.out.println(binarySearch(myList, 6));
    }
}
```
