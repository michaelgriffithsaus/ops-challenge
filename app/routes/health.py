from flask_restful import Resource

class Health(Resource):

    """
        Health check service responding at /health
        Users will query the health check endpoint to confirm that app is in a usable state.
        Health will return a server error when the service is not healthy.
    """

    def get(self):

        if self.check_health():
            response = 200
            status_text = "UP"
        else:
            response = 500
            status_text = "DOWN"

        return {'status': status_text}, response

    def check_health(self, healthy=True):

        """
            Currently only returns a healthy status unless a false healthy state is passed in
            (which can be used for unit testing).
            This function should be expanded to check the status of downstream services such as
            queues, databases and external endpoints as they are added to the app.
        """

        if not healthy:
            return False

        return healthy
