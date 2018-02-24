from flask_restful import Resource

class HelloWorld(Resource):

    """
        Standard Hello world function.
        Intended to be called from the root of the API service.
    """

    def get(self):
        return {'hello': 'world'}
