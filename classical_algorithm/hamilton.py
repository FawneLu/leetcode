# Python program for solution of 
# hamiltonian cycle problem 

class Graph(): 
    def __init__(self, vertices): 
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)] 
        self.V = vertices 
        self.all_path = []
        self.total_weight = float("inf")
        self.circle = None

    def isSafe(self, v, pos, path): 
        # Check if current vertex and last vertex 
        # in path are adjacent 
        if self.graph[ path[pos-1] ][v] == 0: 
            return False

        # Check if current vertex not already in path 
        for vertex in path: 
            if vertex == v: 
                return False

        return True

    # A recursive utility function to solve 
    # hamiltonian cycle problem 
    def hamCycleUtil(self, path, pos): 

        # base case: if all vertices are 
        # included in the path 
        if pos == self.V: 
            # Last vertex must be adjacent to the 
            # first vertex in path to make a cyle 
            if self.graph[ path[pos-1] ][ path[0] ] == 1: 
                self.all_path.append(list(path))
                if sum(path) < self.total_weight:
                    self.total_weight = sum(path)
                    self.circle = list(path)


                return True
            else: 
                return False

        # Try different vertices as a next candidate 
        # in Hamiltonian Cycle. We don't try for 0 as 
        # we included 0 as starting point in in hamCycle() 
        for v in range(1,self.V): 

            if self.isSafe(v, pos, path) == True: 

                path[pos] = v 

                self.hamCycleUtil(path, pos+1)
                # Remove current vertex if it doesn't 
                # lead to a solution 
                path[pos] = -1



    def hamCycle(self): 
        path = [-1] * self.V 

        ''' Let us put vertex 0 as the first vertex 
            in the path. If there is a Hamiltonian Cycle, 
            then the path can be started from any point 
            of the cycle as the graph is undirected '''
        path[0] = 0

        self.hamCycleUtil(path,1) 


g1 = Graph(5) 
g1.graph = [ [0, 2, 1, 1, 0], [2, 0, 1, 1, 1], 
            [1, 1, 0, 0, 5],[1, 1, 0, 0, 3], 
            [0, 1, 5, 3, 0]] 

# Print the solution 
g1.hamCycle();
print("all the path of hamiltonian circuits: ")
for path in g1.all_path:
    print(path)
print("")
print("the min weight is: {}".format(g1.total_weight))
print("the min weight path is: {}".format(g1.circle))
