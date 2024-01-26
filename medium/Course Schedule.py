from typing import List
from collections import defaultdict


def create_edges(prerequisites: list) -> dict:
    edges = defaultdict(list)
    for edge in prerequisites:
        edges[edge[0]].append(edge[1])
    return edges


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    edges = create_edges(prerequisites)
    seen = []
    visited = []
    for vertex in range(numCourses):
        if not traverse_graph(edges, vertex, seen, visited):
            return False
    return True


def traverse_graph(edges, vertex, seen, visited):
    if vertex in visited:
        return True
    if vertex in seen:
        return False
    seen.append(vertex)
    for cur_edge in edges[vertex]:
        if not traverse_graph(edges, cur_edge, seen, visited):
            return False

    visited.append(vertex)
    return True
