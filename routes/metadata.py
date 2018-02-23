import json
from flask_restful import Resource


class Metadata(Resource):

    """
        The Metadata class will present users with the applicaitons build information.
        This will allow users to identify which version (and commit) of the service is running. 
        This is achieved by serving the build.json which is generated during CI
    """

    def get(self):
        file = open('build.json', 'r')
        properties = file.read()
        file.close()

        return json.loads(properties)
