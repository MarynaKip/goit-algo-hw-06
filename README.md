# goit-algo-hw-06
# Writing the README.md file with a summary of all tasks

readme_content = """
# Graph Pathfinding and Shortest Path Algorithms

### Task 1: Graph Model of a Real Network
- A graph was created to represent a city's transportation network.
- The graph consists of 8 vertices (bus stops) and 9 edges (bus routes).
- Main Characteristics:
  - Number of vertices: 8
  - Number of edges: 9
  - Degrees of vertices:
    - Stop A: 3
    - Stop B: 2
    - Stop C: 2
    - Stop D: 3
    - Stop E: 2
    - Stop F: 2
    - Stop G: 2
    - Stop H: 2

### Task 2: DFS and BFS Algorithms
- **DFS Path from Stop A to Stop G:** ['Stop A', 'Stop B', 'Stop D', 'Stop E', 'Stop F', 'Stop G']
- **BFS Path from Stop A to Stop G:** ['Stop A', 'Stop H', 'Stop G']
- **Comparison:**
  - DFS explores deeper into the graph first, resulting in a longer path through more intermediate stops.
  - BFS explores in breadth, finding the shortest path in terms of the number of edges between stops.

### Task 3: Dijkstra's Algorithm for Shortest Path
- Weights (travel times in minutes) were added to the graph.
- **Shortest Path from Stop A to Stop G using Dijkstra's Algorithm:** ['Stop A', 'Stop H', 'Stop G']
- **Total Travel Time:** 12 minutes
- Dijkstra's algorithm finds the shortest path based on total travel time, not just the number of stops.
