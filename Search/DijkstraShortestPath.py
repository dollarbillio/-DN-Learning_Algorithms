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
Cost to travel from start_node to other nodes
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

def find_lowest_cost_node(costs):
    ''' 
    This function will return the node
    with lowest cost that is not in the processed list
    '''
    # assuming that lowest_cost = infinity
    lowest_cost = float("inf")
    # default == None incase | final destination has no neighbor_output node
    lowest_cost_node = None
    ''' Iterate over whole items in costs to compare costs'''
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost 
            lowest_cost_node = node
        
    return lowest_cost_node

# +---------------------------------+
# | Main Dijkstra's
# +---------------------------------+
node = find_lowest_cost_node(costs)

while node is not None:
    # Distance from "start" to its neighbor_nodes
    # int output
    cost_to_node = costs[node]
    # neighbors of the current node. Type: dict
    neighbor_node = graph[node]

    # for [c, d, e]  in neighbors dictionary of b
    for n in neighbor_node.keys():
        # new_cost = cost to b from start + cost from b to the current neighbor
        new_cost = cost_to_node + neighbor_node [n]

        ''' 
        Cross check the table cost 
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
    processed.append(node)
    # Call the function again
    node = find_lowest_cost_node(costs)

print (costs)
print (parents)

    
