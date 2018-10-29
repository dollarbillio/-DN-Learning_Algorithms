# Hash Table:
---
* **Cache**: Using Hash_Table to memorize data instead of recalculating
---
**Collision**:
- Normally, search/delete/insert time = O(1) => Very fast operation
- A linked_list (values) is mapped to a slot_key in the hash table
  * Making the search/delete/insert = O(n) => Like normal linked_list

<p align="center">
  <img width="350" height="350" src="https://javaconceptoftheday.com/wp-content/uploads/2016/02/HashMapInternalStructure.png">
</p>

---
* **Load Factor**: number of used slots / predetermined_len(slots)
  
