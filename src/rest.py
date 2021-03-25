from flask import Flask, request
from flask_restful import Resource,Api,reqparse
import main

#starting flask app
app = Flask(__name__)
api = Api(app)

#initializing the game object
pekingExpress = main.PekingGame(0,0)

#initializing the request parser
map_post_args = reqparse.RequestParser()
location_post_args = reqparse.RequestParser()
competitorLocations_post_args = reqparse.RequestParser()

#The required request arguments for the POST method on '/game'
map_post_args.add_argument("locations", help= "Locations are required",  type=str, required =True)
map_post_args.add_argument("connections",help= "Connections are required", type=str, required =True)


#The required request arguments for the POST method on '/location'
location_post_args.add_argument("startlocation",help= "Start location is required", type=int, required =True)

#The required request arguments for the POST method on '/updateCompetitorLocation'
competitorLocations_post_args.add_argument("groupid",help= "group id is required", type=int, required =True)
competitorLocations_post_args.add_argument("location",help= "location is required", type=int, required =True)


#class resources
class Map(Resource):
    def post(self):
        args = map_post_args.parse_args()
        map = request.json
        print(map["locations"])
        pekingExpress.initializeMap(map)
        
class NextMove(Resource):
    def get(self):
        nextMove = pekingExpress.nextMove()
        return {'nextMove': nextMove}

class Location(Resource):
    def post(self):
        args = location_post_args.parse_args()
        startLocation = args["startlocation"]
        pekingExpress.setStartLocation(startLocation)

class UpdateCompetitorLocation(Resource):
    def post(self):
        args = competitorLocations_post_args.parse_args()
        groupId = args["groupid"]
        location = args["location"]
        pekingExpress.updateCompetitorLocation(groupId,location)

#routes
api.add_resource(Map,'/initializeMap')
api.add_resource(Location,'/location')
api.add_resource(NextMove,'/nextMove')
api.add_resource(UpdateCompetitorLocation,'/updateCompetitorLocation')


#debug
if __name__ == '__main__':
    app.run(debug=True)
