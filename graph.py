import math

class Graph:
    def __init__(self, graph = {}):
        self.graph = graph

    # add a vertex with the specified label. Return the graph.label must be a string or raise ValueError
    def add_vertex(self, label):
        if not isinstance(label, str):
            raise ValueError ("label is not a string")
        if label in self.graph:
            print("Vertex already in graph")
        else:
            self.graph[label] = []
        return self.graph

    # add an edge from vertex srcto vertex destwith weight w. 
    # Return the graph.validate src, dest, and w: raise ValueError if not valid.
    def add_edge(self, src, dest, weight):
        if not isinstance(src, str):
            raise ValueError ("Source is not a string")
        if not isinstance(dest, str):
            raise ValueError ("Destination is not a string")
        if not isinstance(weight, int):
            raise ValueError ("Weight is not an integer")
        if src not in self.graph:
            print("Vertex ", src, " does not exist.")
            # Check if vertex v2 is a valid vertex
        elif dest not in self.graph:
            print("Vertex ", dest, " does not exist.")
        else:
            temp = [dest, weight]
            self.graph[src].append(temp)    

    # float get_weight(src, dest) : Return the weight on edge src-dest(math.inf if no path exists,
    # raise ValueError if src or dest not added to graph).
    def get_weight(self, src, dest):
        if src not in self.graph:
            raise ValueError("Source not in graph")
        if dest not in self.graph:
            raise ValueError("Destination not in graph")
        i = 0 
        inlist = False
        while i < len(self.graph[src]):
            if self.graph[src][i][0] == dest:
                inlist = True 
                break
            i += 1
        if inlist:
            return self.graph[src][i][1]
        if not inlist:
            return math.inf 
        


    # •dfs(starting_vertex): Return a generator for traversing the graph in depth-first order 
    # starting from the specified vertex. Raise a ValueError if the vertex does not exist.
    def dfs(self, starting_vertex):
        def dfs_helper(src, visited):
            visited.add(src)
            yield src
            for neighbour in self.graph[src]:
                if neighbour not in visited:
                    dfs_helper(neighbour, visited)
        if starting_vertex not in self.graph:
            raise ValueError ("Starting vertex is not in the graph")
        visited = set()
        yield dfs_helper(starting_vertex, visited)

    # •bfs(starting_vertex): Return a generator for traversing the graph in breadth-first order 
    # starting from the specified vertex. Raise a ValueError if the vertex does not exist.
    def bfs(self, starting_vertex):
        if starting_vertex not in self.graph:
            raise ValueError ("Starting vertex is not in the graph")
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(starting_vertex)
        visited[starting_vertex] = True
        while queue:
            starting_vertex = queue.pop(0)
            for i in self.graph[starting_vertex]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    # •list dijkstra_shortest_path(src, dest): Return a tuple (path length , the list of vertices 
    # on the path from destback to src). If no path exists, return thetuple (math.inf, empty list.)

    # •dict dijkstra_shortest_path(src): Return a dictionary of the shortest weighted path 
    # between srcand all other vertices using Dijkstra's Shortest Path algorithm. 
    # In the dictionary, the key is the vertex label, the value is a tuple (path length , 
    # the list of vertices on the path from keyback to src). 
    def dijkstra_shortest_path(self, src, dest = None):
        pass

    # •__str__: Produce a string representation of the graph that can be used with print().
    def __srt__(self):
        pass