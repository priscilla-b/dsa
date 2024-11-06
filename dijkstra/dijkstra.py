
"""
- You need three hash tables:
    - one for the graph
    - one for the costs (how long it takes to get to each node from the start)
    - one for the parents of each node

- You also need an array to keep track of all the nodes that are already processed 
to avoid processing the same node more than once
"""


def get_shortest_path(costs, graph, parents):
    processed = []
    # start with the node with the lowest cost that hasn't been processed yet
    node = find_lowest_cost_node(costs, processed)

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        # calculate the new cost of each neighbor by adding the current cost
        # of the parent node to its edge weight
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]

            # if the new cost is smaller than its original cost
            # you found a shorter path to the node, so update the costs hash table
            if costs[n] > new_cost:
                costs[n] = new_cost

                # since we found a new path to node n through the current node, 
                # update the parent of node n as the current node
                parents[n] = node
        
        # once the costs for all the neighbors of the node has been updated,
        # mark the node as processed
        processed.append(node)

        # find the new lowest node and repeat the process
        node = find_lowest_cost_node(costs, processed)

    # return the weight of the shortest path
    return costs["fin"]


def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:
        # get the cost and neighbors of that node
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
        


graph = {}

# store the weight of each node edge as the value of the hash map
graph["start"] = {}
graph["start"]["a"] = 5
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 2

graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["d"] = 7

graph["c"] = {}
graph["c"]["d"] = 6
graph["c"]["fin"] = 3

graph["d"] = {}
graph["d"]["fin"] = 1

graph["fin"] = {}


# using infinity to represent nodes whose costs are not known yet
infinity = float("inf")
costs = {}
costs["a"] = 5
costs["b"] = 2
costs["c"] = infinity
costs["d"] = infinity
costs["fin"] = infinity

# parent of a node is the node it was reached from
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
parents["fin"] = None


print(get_shortest_path(costs, graph, parents))