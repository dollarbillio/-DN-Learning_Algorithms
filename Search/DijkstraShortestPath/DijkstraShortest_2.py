# +------------------------------------------+
# |Create a graph with neighbors and distance
# | from node -> neighbors
# +------------------------------------------+
graph = {}
graph["START"] = {}
graph["A"] = {}
graph["B"] = {}
graph["C"] = {}
graph["D"] = {}
graph ["FIN"] = {}

graph["START"]["B"] = 5
graph["START"]["A"] = 2

graph["B"]["C"] = 4
graph["B"]["D"] = 2

graph["A"]["B"] = 8
graph["A"]["D"] = 7

graph["C"]["D"] = 6
graph["C"]["FIN"] = 3

graph["D"]["FIN"] = 1

# +---------------------------------+
# | Create a cost table from "START"
# |  to other nodes
# +---------------------------------+
nodes_costs = {}
infinity = float("inf")
nodes_costs["B"] = 5
nodes_costs["A"] = 2
nodes_costs["C"] = infinity
nodes_costs["D"] = infinity
nodes_costs["FIN"] = infinity

# +------------------------------------------+
# | Create a parent dictionary to keep track
# | of previous node leading to this node
# +------------------------------------------+
parents = {}
parents["B"] = "START"
parents["A"] = "START"
parents["C"] = None
parents["D"] = None
parents["FIN"] = None

# +---------------------------+
# | Create an array to check 
# |  if the node is processed
# +---------------------------+
processed = []

# +-----------------------------------------------+
# | Find the lowest_cost_node and return the node
# +-----------------------------------------------+
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in nodes_costs:
        if nodes_costs[node] < lowest_cost and node not in processed:
            lowest_cost = nodes_costs[node]
            lowest_cost_node = node

    return lowest_cost_node

# Find the lowest cost_node initially with values from costs
lowest_node = find_lowest_cost_node(nodes_costs)

while not (lowest_node == None):
    # Find the neighbor_nodes of the current nodes
    neighbor_nodes = graph[lowest_node]
    init_cost_to_node = nodes_costs[lowest_node]
    
    for node in neighbor_nodes.keys():
        # update the neighbors_cost of current node
        new_cost = init_cost_to_node + neighbor_nodes[node]
        # Compare the cost_to_node already in costs and new cost
        if nodes_costs[node] > new_cost:
            nodes_costs[node] = new_cost
            parents[node] = lowest_node
    
    processed.append(lowest_node)
    lowest_node = find_lowest_cost_node(nodes_costs)

print (parents)
print (nodes_costs)
