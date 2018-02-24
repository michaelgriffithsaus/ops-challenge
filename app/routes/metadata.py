import json
import pkg_resources
import os
from flask_restful import Resource


class Metadata(Resource):

    """
        The Metadata class will present users with the applicaiton's build information.
        This will allow users to identify which version (and commit) of the service is running.
        This is achieved by serving content from the build.txt file which is populated during CI.
    """

    def get(self):

        # Find the build.txt file in the application
        # TODO I'd prefer to pass in build.txt as an env variable so that this doesnt break later
        build_file_path = pkg_resources.resource_filename('app', 'build.txt')

        if os.path.isfile(build_file_path):
            with open(build_file_path, 'r') as file:
            
                try:
                    properties = dict(line.rstrip().split("=") for line in file)
                    return properties
                except Exception as e:
                    return {"Error encountered reading metadata file: " + e.message} , 500

        else:
            return {"Unable to open metadata file. File not found"} , 500

