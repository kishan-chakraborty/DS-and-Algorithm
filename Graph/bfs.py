def bfs(graph, start):
    # Create a queue for BFS and mark the start node as visited
    queue = [start]
    visited = set([start])

    # List to store the order of nodes visited
    bfs_order = []

    while queue:
        # Dequeue a vertex from the queue
        node = queue.popleft()
        bfs_order.append(node)

        # Get all adjacent vertices of the dequeued vertex
        for neighbor in graph[node]:
            if neighbor not in visited:
                # Mark the neighbor as visited and enqueue it
                visited.add(neighbor)
                queue.append(neighbor)

    return bfs_order


if __name__ == "__main__":
    # Example graph as an adjacency list.
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    # Running BFS starting from node 'A'
    bfs_order = bfs(graph, "A")
    print("BFS Order:", bfs_order)
