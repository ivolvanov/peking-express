import json
from collections import defaultdict 

class PekingGame(object):
    map_dict = {}
    startLocation = 0
    currentLocation = 0
    nrOfLocations = 0
    criticalLocations = []
    sources = []
    targets = []
    prices = []
    occupiedLocations = []
    turn = 0
    budget = 0

    # constuctor
    # initializes the initial state of the game
    def __init__(self, testfileLocation):
        testfile = []
        f = open(testfileLocation, "r")
        for line in f:
            testfile.append(line.strip())
        f.close()
        map = json.loads(testfile[0])
        startLocation = json.loads(testfile[1])
        budget = json.loads(testfile[2])
        occupiedLocations = json.loads(testfile[3])  
        
        self.setStartLocation(startLocation)
        self.updateOccupiedLocations(occupiedLocations , self.turn)
        self.setBudget(budget)
        self.initializeMap(map)

    def initializeMap(self, map):
        self.map_dict = map
        self.nrOfLocations = self.map_dict['locations']['number']
        self.criticalLocations = self.map_dict['locations']['critical']
        self.sources = self.map_dict['connections']['source']
        self.targets = self.map_dict['connections']['target']
        self.prices = self.map_dict['connections']['price']

        self.graph = Graph(self.nrOfLocations)
        for i in range(len(self.sources)):
            self.graph.addEdge(self.sources[i], self.targets[i], self.prices[i])
            self.graph.addEdge(self.targets[i], self.sources[i], self.prices[i])

        self.graph.generatePaths(self.startLocation, 88)
        self.graph.paths.sort(key=len)
        self.graph.calculatePathPrices()

    def setStartLocation(self, startLocation_param : int):
        self.startLocation = startLocation_param

    def setBudget(self,budget_param : int):
        self.budget = budget_param

    def updateTurnCount(self):
        self.turn +=1

    # updates the occupiedLocations per turn
    def updateOccupiedLocations(self,locationList , turn : int ):
        #self.competitorLocations[groupid - 1] = location
        self.occupiedLocations.append(locationList)

    

    def nextMove(self) -> int:

        #algorithm goes BRRRRRRRRRRR

        updateTurnCount()
        return 0
        
class Graph: 
   
    def __init__(self, vertices): 
        self.V = vertices          
        self.graph = defaultdict(list) 
        self.paths = list()
        self.vertices = []
        self.prices = []
        self.pathPrices = []
 
    def addEdge(self, u, v, price): 
        self.graph[u].append(v)
        self.vertices.append((u, v))
        self.prices.append(price)

    def calculatePathPrices(self):
        for i in range(len(self.paths)):
            currentPathPrice = 0
            for q in range(len(self.paths[i]) - 1):
                index = self.vertices.index((self.paths[i][q], self.paths[i][q+1]))
                currentPathPrice += self.prices[index]

            self.pathPrices.append(currentPathPrice)

    def pathsUtil(self, u, d, visited, path): 
        visited[u]= True
        path.append(u)
  
        if u == d:
            currPath = path[:]
            self.paths.append(currPath)
        else: 
            for i in self.graph[u]: 
                if visited[i] == False: 
                    self.pathsUtil(i, d, visited, path) 
                      
        path.pop() 
        visited[u] = False
   
    def generatePaths(self, s, d): 
        visited =[False] * 89 
        path = []
        self.pathsUtil(s, d, visited, path)        

game = PekingGame("./test/test1.txt")
print(game.graph.paths)
print(game.graph.pathPrices)