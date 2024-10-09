# Dijkstra's algorithm

Breadth-first search helps to find the smallest number of edges (segments) it takes to get to a destination (the shortest path), but it does not really take into account the actual length of the edges (the distance from one node to another along the edge).
If it did, there could be other paths that might not necessarily be the shortest paths, but they'll have smaller distances along the edges, which when combined can produces a path with a smaller distance (the fastest path).
This is what Dijktra's algorithm does - finds the fastest path between two points.