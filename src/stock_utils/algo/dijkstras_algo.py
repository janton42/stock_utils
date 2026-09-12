"""Dijkstra's shortest path algorithm implementation."""

import itertools
from heapq import heappush, heappop

# Priority queue implementation
class PriorityQueue:
    """Priority queue used by Dijkstra's shortest-path algorithm.

    Entries are stored as ``[priority, count, task]`` tuples so tasks can be
    compared by priority while preserving insertion order for ties.
    """

    def __init__(self):
        """Initialize the priority queue."""
        self.pq = []				# List of entries arranged in a heap
        self.entry_finder = {}			# mapping of tassk to entries
        # REMOVED = '<removed-task>'		# placeholder for a removed task
        self.counter = itertools.count()	# unique sequence count

    def __len__(self):
        """Return the number of queued tasks."""
        return len(self.pq)

    def add_task(self, priority, task):
        """Add a task to the queue or update its priority when present.

        Args:
            priority: Relative priority for the task.
            task: Task identifier to add or update.

        Returns:
            The queue instance for chaining convenience.
        """
        if task in self.entry_finder:
            self.update_priority(priority, task)
            return self
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def update_priority(self, priority, task):
        """Update the priority for an existing queued task.

        Args:
            priority: New priority value.
            task: Task identifier to update.
        """
        entry = self.entry_finder[task]
        count = next(self.counter)
        entry[0], entry[1] = priority, count

    def pop_task(self):
        """Remove and return the next task with the lowest priority.

        Returns:
            A tuple of ``(priority, task)`` for the next task.

        Raises:
            KeyError: If the queue is empty.
        """
        while self.pq:
            priority, count, task = heappop(self.pq)
            del self.entry_finder[task]
            return priority, task
        raise KeyError('YOU FAIL! pop from an empty priority queue')


class Graph:
    """Graph container backed by an adjacency list."""

    def __init__(self, adjacency_list):
        """Initialize the graph with an adjacency list.

        Args:
            adjacency_list: Mapping of vertices to their outgoing edges.
        """
        self.adjacency_list = adjacency_list


class Vertex:
    """Graph vertex containing a value."""

    def __init__(self, value):
        """Initialize a vertex.

        Args:
            value: Data stored on the vertex.
        """
        self.value = value


class Edge:
    """Weighted edge connecting a vertex to another vertex."""

    def __init__(self, distance, vertex):
        """Initialize an edge.

        Args:
            distance: Cost of traversing the edge.
            vertex: Destination vertex reached by the edge.
        """
        self.distance = distance
        self.vertex = vertex


def dijkstra(graph, start, end):
    """Find and print the shortest path from ``start`` to ``end``.

    Args:
        graph: Graph whose adjacency list contains weighted ``Edge`` objects.
        start: Starting vertex.
        end: Destination vertex.

    Returns:
        None. The shortest distance and path are printed to stdout.
    """
    previous = {v: None for v in graph.adjacency_list.keys()}
    visited = {v: False for v in graph.adjacency_list.keys()}
    distances = {v: float('inf') for v in graph.adjacency_list.keys()}
    distances[start] = 0
    queue = PriorityQueue()
    queue.add_task(0, start)
    path = []
    while queue:
        removed_distance, removed = queue.pop_task()
        visited[removed] = True
        if removed is end:
            while previous[removed]:
                path.append(removed.value)
                removed = previous[removed]
            path.append(start.value)
            print(f'shortest distance to {end.value}: ', distances[end])
            print(f'path to {end.value}: ', path[::-1])
            return

        for edge in graph.adjacency_list[removed]:
            if visited[edge.vertex]:
                continue
            new_distance = removed_distance + edge.distance
            if new_distance < distances[edge.vertex]:
                distances[edge.vertex] = new_distance
                previous[edge.vertex] = removed
                queue.add_task(new_distance, edge.vertex)
    return

# test
vertices = [Vertex('A'), Vertex('B'), Vertex('C'), Vertex('D'), Vertex('E'), Vertex('F'), Vertex('G'), Vertex('H')]
A, B, C, D, E, F, G, H = vertices
adj_list = {
    A: [Edge(1.8, B), Edge(1.5, C), Edge(1.4, D)],
    B: [Edge(1.8, A), Edge(1.6, E)],
    C: [Edge(1.5, A), Edge(1.8, E), Edge(2.1, F)],
    D: [Edge(1.4, A), Edge(2.7, F), Edge(2.4, G)],
    E: [Edge(1.6, B), Edge(1.8, C), Edge(1.4, F), Edge(1.6, H)],
    F: [Edge(2.1, C), Edge(2.7, D), Edge(1.4, E), Edge(1.3, G), Edge(1.2, H)],
    G: [Edge(2.4, D), Edge(1.3, F), Edge(1.5, H)],
    H: [Edge(1.6, E), Edge(1.2, F), Edge(1.5, G)]
}

test_graph = Graph(adj_list)

dijkstra(test_graph, start=A, end=H)
