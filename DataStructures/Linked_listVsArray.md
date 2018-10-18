# Linked_List Vs Array

* **memory** is like a collection of boxes
* **array**: size pre-designated memory boxes near each other. If Adding item, will need to move each item to a new box that can fit pre-designated more task
* **linked_list** is boxes connected, not necessarily near each other
---
### **Access Element**
* **Array**: Can access element very fast, usually by index: list_1[0] -> O(1)
* **Linked_list**: Have to travel through the sequence -> O(n)
---
### **Insert Element**
* **Array**: insert at ith position will have to **shift** many/all values by an amount -> O(n)
* **Linked_list**: insert at any place if you know the position of connecting nodes -> O(1)
---
### **Delete Element**
* **Array**: shift elements -> O(n)
* **Linked_list**: same as above -> O(1)
