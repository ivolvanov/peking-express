import json
from collections import defaultdict


class PekingGame(object):
    map_dict = {}
    startLocation = 0
    currentLocation = 0
    nrOfLocations = 0
    destination = 88
    criticalLocations = []
    sources = []
    targets = []
    prices = []
    occupiedLocations = []

    # stores the locations occupied for the current turn
    currentOccupiedLocations = []
    turn = 0
    budget = 0

    # stores the path that will be taken
    chosenPath = []
    stepInPath = 0

    # same as chosen path, but with waiting around if critical locations occupied
    finalPath = []

    def __init__(self, testfileLocation):
        testfile = []
        f = open(testfileLocation, "r")

        for line in f:
            testfile.append(line.strip())
        f.close()

        map = json.loads(testfile[0])
        startLocation = int(testfile[1])
        budget = int(testfile[2])
        self.occupiedLocations = json.loads(testfile[3])

        self.setStartLocation(startLocation)
        self.updateOccupiedLocations()
        self.setBudget(budget)
        self.initializeMap(map)

        # with initialization of the object, the final path is constructed
        # it only has to be printed
        self.generateGraph()
        self.pickPath()     
        self.generateFinalPath()   

    def initializeMap(self, map):
        self.map_dict = map
        self.nrOfLocations = self.map_dict['locations']['number']
        self.criticalLocations = self.map_dict['locations']['critical']
        self.sources = self.map_dict['connections']['source']
        self.targets = self.map_dict['connections']['target']
        self.prices = self.map_dict['connections']['price']   

    def setStartLocation(self, startLocation_param: int):
        self.startLocation = startLocation_param

    def setBudget(self, budget_param: int):
        self.budget = budget_param

    def updateTurnCount(self):
        self.turn += 1

    # updates the occupiedLocations per turn
    def updateOccupiedLocations(self):
        if self.turn > len(self.occupiedLocations) or self.turn == 0:
            self.currentOccupiedLocations = []
        else:
            self.currentOccupiedLocations = self.occupiedLocations[self.turn - 1]

    def generateGraph(self):
        self.graph = Graph(self.nrOfLocations)
        for i in range(len(self.sources)):
            self.graph.addEdge(
                self.sources[i], self.targets[i], self.prices[i])
            self.graph.addEdge(
                self.targets[i], self.sources[i], self.prices[i])

        self.graph.generateAllPaths(self.startLocation, self.destination)
        self.graph.paths.sort(key=len)
        self.graph.calculatePathPrices()

    # makes sure that the chosen path is the shortest one within the given budget
    def pickPath(self):
        i = 0
        while self.graph.pathPrices[i] > self.budget:
            i += 1

        self.chosenPath = self.graph.paths[i]

    def nextMove(self):                
        self.updateOccupiedLocations()
        if self.stepInPath != 0:
            self.updateTurnCount() # because the first iteration is turn 0

        # if the next location in our path is taken and o
        if (self.chosenPath[self.stepInPath] in self.criticalLocations) and (self.chosenPath[self.stepInPath] in self.currentOccupiedLocations):
            return self.chosenPath[self.stepInPath - 1]            
        else:
            self.stepInPath += 1
            return self.chosenPath[self.stepInPath - 1]       

        

    def generateFinalPath(self):
        while self.chosenPath[self.stepInPath] != self.destination:
            self.finalPath.append(self.nextMove())

        self.finalPath.append(88)


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
                index = self.vertices.index(
                    (self.paths[i][q], self.paths[i][q+1]))
                currentPathPrice += self.prices[index]

            self.pathPrices.append(currentPathPrice)

    def pathsUtil(self, u, d, visited, path):
        visited[u] = True
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

    def generateAllPaths(self, s, d):
        visited = [False] * 89
        path = []
        self.pathsUtil(s, d, visited, path)


game = PekingGame("./test/test4.txt")
print(game.finalPath)
