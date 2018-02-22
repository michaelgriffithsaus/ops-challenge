from flask_restful import Resource
import json

class Metadata(Resource):

    def get(self):
        file = open('build.properties', 'r')
        properties = file.read()
        file.close()
        
        return json.loads(properties)
