# Greedy Algorithms

Solves a problem with this principle: at each step, pick the ***locally optimum*** solution, and in the end you will arrive at the globally optimum solution.
It doesn't always get the optimal solution, but it will get close.

There are situations where you don't need to get the perfect solution, and that's when algorithm works.

Greedy algorithms are ***approximation algorithms*** and are judged by:
- how fast they are and 
- how close they are to the optimal solution

** Dijkstra is a greedy algorithm


## NP-complete problems
NP-complete problems are problems that are hard to solve and have been deemed impossible to have an efficient optimal solution (i.e. it is not possible to write a perfect solution that can solve them efficiently)
An example is the set covering problem and the traveling salesperson problem.

### The set covering problem
This is one of the problems that are best solved using an approximation algorithm like the greedy algorithm, since the optimal solution is not efficient.

An example of the set-covering problem: given a number of radio stations and the states they play at. Suppose you want to cover a given number of states, but cannot play at all the radio stations due to cost constrainst.  You pick the lowest number (smallest set) of radio stations you can play at such that all states are covered.

The optimal solution to this problem involves listing every possible subset of stations and then picking the smallest subset of these stations that cover all the needed states. This will result in 2^n subsets (where n is the number of stations) and will take O(2^n) time to compute, which is not very efficient if you have a large number of stations.

Greedy algorithm can find the closest optimal answer to the problem in a faster time through these steps:
- pick the station that covers the most states that haven't been covered yet.
- repeat until all the states are covered

The greedy algorithm runs in O(n^2) time.

### The traveling salesperson problem
A salesperson has to visit a number of cities and he's trying to figure out the shortest route that will enable him visit all the cities.

To solve this problem, you'd first have to calculate all the possible number of routes that covers all the given cities and then pick the shortest one. 

If you have to cover two cities, then you have just two routes: from City A to City B and from City B to City A.
If you have 3 cities, you have 6 routes: 2 for each city you can start at. i.e. 3 * 2 = 6
If you have 4 cities, and you pick a start city, you have 3 cities left, which also have 6 routes, making it 4 * 6 = 24 routes.

From this we can draw a pattern that the relationship between the number of cities and the possible routes to be covered is a **factorial** relationship. i.e routes = n!, where n is the number of cities.

If you have 10 cities, 10! is 3,628,800. This makes the number of possible routes become large too quickly, making it really really slow to solve for an optimum solution.

A good approximation for this problem is this:
- pick an arbitrary start city
- each time the traveling salesperson has to pick the next city, pick the closest unvisited city.


### Identifying NP-complete problems
- algorithm(solution) runs quickly with small number of inputs but really slows down when input size increases
- problems involving all combinations of something are usually np-complete
- if you have to calculate "every possible version" of x because you can't break it down into smaller problems
- if your problem involves a sequence (such as sequence of cities like in traveling salesperson) and it's hard to solve
- if your problem involves a set(like a set of radio stations) and it's hard to solve
- if you can restate your problem as the set-covering problem or the traveling-salesperson problem
