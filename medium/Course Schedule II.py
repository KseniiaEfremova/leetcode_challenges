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


def findOrder(numCourses: int, prerequisites: List[List[int]]):
    edges = create_edges(prerequisites)
    seen = []
    visited = []
    for vertex in range(numCourses):
        res = traverse_graph(edges, vertex, seen, visited)
        if not res:
            return []
    return visited


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
