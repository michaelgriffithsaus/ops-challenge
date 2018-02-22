from flask_restful import Resource
import requests

class Health(Resource):

    def get(self):

        status = "DOWN"
        response = 500   

        health = self.checkHealth()

        if health:
            response = 200
            status = "UP"

        return {'Status': status}, response

    
    def checkHealth(self):
        return True