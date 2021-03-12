import json

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


# if __name__ == '__main__':
#     with open('test.json') as f:
#         game = PekingGame(f, 3)