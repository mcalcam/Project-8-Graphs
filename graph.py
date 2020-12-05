class Graph:
    def __init__(self):
        pass

    # add a vertex with the specified label. Return the graph.label must be a string or raise ValueError
    def add_vertex(self, label):
        pass

    # add an edge from vertex srcto vertex destwith weight w. 
    # Return the graph.validate src, dest, and w: raise ValueError if not valid.
    def add_edge(self, src, dest, weight):
        pass

    # float get_weight(src, dest) : Return the weight on edge src-dest(math.inf if no path exists,
    # raise ValueError if src or dest not added to graph).
    def get_weight(self, src, dest):
        pass

    # •dfs(starting_vertex): Return a generator for traversing the graph in depth-first order 
    # starting from the specified vertex. Raise a ValueError if the vertex does not exist.
    def dfs(self, starting_vertex):
        pass

    # •bfs(starting_vertex): Return a generator for traversing the graph in breadth-first order 
    # starting from the specified vertex. Raise a ValueError if the vertex does not exist.
    def bfs(self, starting_vertex):
        pass

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
