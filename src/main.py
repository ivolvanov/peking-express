import json
from collections import defaultdict 


#paths = []
class PekingGame(object):
    map_dict = {}
    startLocation = 0
    currentLocation = 0
    nrOfLocations = 0
    criticalLocations = []
    sources = []
    targets = []
    prices = []
    competitorLocations = [0] * 9

    def __init__(self, map, startLocation):
        self.map = map
        self.setStartLocation(startLocation) 
        self.currentLocation = startLocation  
        #self.initializeMap(map) 


    def initializeMap(self, map):
        #self.map_dict = json.load(map)
        self.map_dict = map
        self.nrOfLocations = self.map_dict['locations']['number']
        self.criticalLocations = self.map_dict['locations']['critical']
        self.sources = self.map_dict['connections']['source']
        self.targets = self.map_dict['connections']['target']
        self.prices = self.map_dict['connections']['price']


    def setStartLocation(self, startLocation_param : int):
        self.startLocation = startLocation_param

    # IMPORTANTE - the competitorLocations list stores the location of group n at index n-1
    # i.e. the location of group 3 is at competitorLocations[2]
    def updateCompetitorLocation(self, groupid : int, location : int):
        self.competitorLocations[groupid - 1] = location

    def nextMove(self) -> int:

        return 0
        
class Graph: 
   
    def __init__(self, vertices): 

        self.V = vertices  
        
        self.graph = defaultdict(list) 

        self.paths = list()
 
    def addEdge(self, u, v): 
        self.graph[u].append(v) 

    def pathsUtil(self, u, d, visited, path): 

        visited[u]= True
        path.append(u) 
  
        if u == d:
            currPath = path[:]
            self.paths.append(currPath)
            print(path)
        else: 
            for i in self.graph[u]: 
                if visited[i]== False: 
                    self.pathsUtil(i, d, visited, path) 
                      
        path.pop() 
        visited[u] = False
   
    def generatePaths(self, s, d): 

        visited =[False]*(self.V) 

        path = []

        self.pathsUtil(s, d, visited, path) 


   
   
   
# Create a graph given in the above diagram 
g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(0, 3) 
g.addEdge(2, 0) 
g.addEdge(2, 1) 
g.addEdge(1, 3) 
   
s = 2 ; d = 3
print ("Following are all different paths from % d to % d :" %(s, d)) 
g.generatePaths(s, d) 
print(g.paths)

# This code is contributed by Neelam Yadav


# if __name__ == '__main__':
#     with open('test.json') as f:
#         game = PekingGame(f, 3)