from collections import deque

# implementing a graph showing an entity (you) and its neighbors
# going to search through all neighbors until I get one who sells mangos

def breadth_first(graph:dict, start:str):
    # create a queue to add the node values for search
    search_queue = deque()
    # add initial list of people to search using the starting point
    search_queue += graph[start]

    # keeping a list to tracked people who have been searched
    searched = []

    while search_queue:
        current = search_queue.popleft()

        # avoid searching someone who has been searching again to prevent
        # possible infinite loops
        if not current in searched:
            if(person_is_seller(current)):
                return current      
            # if person is not mango seller, add all their neighbors to queue
            search_queue += graph[current]
            searched.append(current)





def person_is_seller(name):
    return name[-1] == 'm'


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

print(breadth_first(graph, "you"))