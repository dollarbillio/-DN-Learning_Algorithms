# +-------------------------------+
# | Create Neighbor_Graph
# +-------------------------------+
'''
dictionary in dictionary
{node:{neighbor:distance}}
'''
graph = {}
# Neighbor of start_node
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

# Neighbor of a_node
graph["a"] = {}
graph["a"]["fin"] = 1

# neighbor of b_node
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

# destination has no node
graph["fin"] = {}
# +-----------------------------------------------+
# | Create table with the lowest costs for "start" 
# +-----------------------------------------------+

'''
Cost to travel from startNode to other nodes
{node_a:distance_from_a}
'''

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# +-----------------------+
# | Create a parents table
# +-----------------------+

'''
{node:previous_node}
'''
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# +---------------------------------+
# | Create an array to keep track of 
# | all nodes processed
# +---------------------------------+
processed = []

# +---------------------------------+
# | Find the lowest cost-node 
# | that you haven't processed yet
# +---------------------------------+

def FindLowestCostNode(costs):
    ''' 
    function returns the node s.t ("start" -> node) = lowestCost
    and node not in the processed list
    '''
    # assuming that lowestCost = infinity
    lowestCost = float("inf")
    # default == None incase | final destination has no neighbor_output node
    lowestCostNode = None
    ''' Iterate over whole items in costs to compare costs'''
    for node in costs:
        cost = costs[node]
        if cost < lowestCost and not (node in processed):
            lowestCost = cost 
            lowestCostNode = node
        
    return lowestCostNode

# +---------------------------------+
# | Main Dijkstra's
# +---------------------------------+
lowestCostNode = FindLowestCostNode(costs)

while lowestCostNode != None:
    # Distance from "start" to its neighbor_nodes
    # int output
    costToNode = costs[lowestCostNode]
    # neighbors of the current node. Type: dict
    lowestCostNodeNeighbor = graph[lowestCostNode]

    # for [c, d, e]  in neighbors dictionary of b
    for node in lowestCostNodeNeighbor.keys():
        # new_cost = startToCurrentNode + bToItsNeighbor
        newCost = costToNode + lowestCostNodeNeighbor[n]

        ''' 
        Cross check the tableCost from "start"
        * is the cost from start to c/not through b) 
        greater than start to c/through b)?
        '''
        if costs[n] > new_cost:
            # update the cost to get to a with shorter path from start
            # if costs['c'] == 6, new_cost == 5 => 
            # update costs['c'] with 5
            costs[n] = new_cost
            # update the previous node as 'b', not start
            parents[n] = node
    
    # add the processed 'b' in the processed list and not processed again
    processed.append(lowestCostNode)
    # Call the function again
    node = FindLowestCostNode(costs)

print (costs)
print (parents)

    
