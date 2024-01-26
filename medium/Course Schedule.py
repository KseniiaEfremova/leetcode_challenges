from typing import List


def create_edges(prerequisites: list) -> dict:
    edges = dict()
    for edge in prerequisites:
        vertex = edge[0]
        if vertex in edges:
            edges[vertex].append(edge[1])
        else:
            edges[vertex] = [edge[1]]
    return edges


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    edges = create_edges(prerequisites)
    seen = []
    visited = []
    vertices = list(edges.keys())
    for vertex in vertices:
        res = traverse_graph(edges, vertex, seen, visited)
        if not res:
            return False
    return True


def traverse_graph(edges, cur_node, seen, visited):
    vertex = cur_node
    if vertex in seen:
        return False
    if vertex in visited:
        return True
    if vertex not in edges:
        visited.append(vertex)
        return True
    seen.append(vertex)
    for cur_edge in edges[vertex]:
        res = traverse_graph(edges, cur_edge, seen, visited)
        if not res:
            return False

    visited.append(vertex)
    seen.pop()
    return True


q = [[1, 2], [1, 5], [1, 6], [5, 6]]
cycle = [[1, 2], [2, 3], [3, 1]]
test = [[1, 4], [2, 4], [3, 1], [3, 2]]
print(canFinish(0, cycle))
