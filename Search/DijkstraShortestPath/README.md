# Dijkstra Shortest Path
---
* Can't be used on negative weighted graph
---
**Components**
* A graph that keeps track of nodes and neighbors
 * ```{node:{neighbor:distance}}```
* A table to update the shortest path from 'start' to node_i
 * ```{nodes:distance}```
* A table to keep track of the previous node that leads to current node 
 * ```{nodes:previous_node}```
* An array to keep track of visited nodes
