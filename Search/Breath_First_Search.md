# BFS
---
* Search the network by the order degree of connection: 1st order co, 2nd_order
* Use Queue (FIFO)
* Running time: 
  * Run through all edges to find the possible edges, then find the shortest path => short_test can also be the longest path
  * Keep adding queue of every person to search
  * Worst Case: O(Vertices + Edges)
---
**BFS.py**
```python
graph = {}
# ["alice", "bob", "clair"] are all connected to "Bob"
graph["pop"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["johny"] = []

from collections import deque

def search(name):
    # Create a deque() class instance
    search_queue = deque()
    search_queue += graph[name]
    # Keep track of people that were searched
    searched = []
    while len(search_queue) > 0:
        person = search_queue.popleft()
        if not person in searched:
            if is_seller(person):
                print (person + " is a seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

def is_seller(person):
    return person[-1] == 'm'

print (search("pop"))
```
