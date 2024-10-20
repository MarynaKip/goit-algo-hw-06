import networkx as nx
import matplotlib.pyplot as plt

# Task 1: Create and visualize a graph model of a real network (city transportation network)
# Let's consider a simplified public transportation network for a city with bus stops.

# Create a graph with nodes as bus stops and edges as bus routes between stops


G = nx.Graph()

# Add nodes (bus stops)
bus_stops = ["Stop A", "Stop B", "Stop C", "Stop D", "Stop E", "Stop F", "Stop G", "Stop H"]
G.add_nodes_from(bus_stops)

# Add edges (bus routes between stops)
routes = [
    ("Stop A", "Stop B"), ("Stop A", "Stop C"),
    ("Stop B", "Stop D"), ("Stop C", "Stop D"),
    ("Stop D", "Stop E"), ("Stop E", "Stop F"),
    ("Stop F", "Stop G"), ("Stop G", "Stop H"),
    ("Stop H", "Stop A")
]
G.add_edges_from(routes)

# Visualize the graph
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', node_size=1500, font_size=10, font_weight='bold', edge_color='gray')
plt.title("City Transportation Network")
plt.show()

# Analyze the main characteristics
num_vertices = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f'Number of vertices: {num_vertices}, Number of edges: {num_edges}, Degrees: {degrees}')


# Task 2: Implement DFS and BFS to find paths in the graph

# Recursive function for DFS
def dfs(graph, start, target, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    
    path.append(start)
    visited.add(start)
    
    if start == target:
        return path
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, target, path.copy(), visited)
            if result:
                return result
    
    return None

# Iterative function for BFS
def bfs(graph, start, target):
    visited = set()
    queue = [(start, [start])]
    
    while queue:
        (vertex, path) = queue.pop(0)
        if vertex not in visited:
            if vertex == target:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                queue.append((neighbor, path + [neighbor]))
    return None

# Testing DFS and BFS on the graph
start_node = "Stop A"
target_node = "Stop G"

dfs_path = dfs(G, start_node, target_node)
bfs_path = bfs(G, start_node, target_node)

print(f'dfs_path: {dfs_path}')
print(f'bfs_path: {bfs_path}')


# Task 3: Add weights to the edges and implement Dijkstra's algorithm

# Adding weights to the graph (representing travel time between stops in minutes)
weighted_routes = [
    ("Stop A", "Stop B", 5), ("Stop A", "Stop C", 7),
    ("Stop B", "Stop D", 3), ("Stop C", "Stop D", 4),
    ("Stop D", "Stop E", 2), ("Stop E", "Stop F", 6),
    ("Stop F", "Stop G", 1), ("Stop G", "Stop H", 4),
    ("Stop H", "Stop A", 8)
]

# Create a weighted graph
G_weighted = nx.Graph()
G_weighted.add_weighted_edges_from(weighted_routes)

# Implementing Dijkstra's algorithm to find the shortest path
def dijkstra(graph, start, target):
    return nx.shortest_path(graph, source=start, target=target, weight='weight'), nx.shortest_path_length(graph, source=start, target=target, weight='weight')

# Finding the shortest path using Dijkstra's algorithm
dijkstra_path, dijkstra_path_length = dijkstra(G_weighted, start_node, target_node)

print(f'dijkstra_path: {dijkstra_path}, dijkstra_path_length: {dijkstra_path_length}')