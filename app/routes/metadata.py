import json
import pkg_resources
import os
from flask_restful import Resource


class Metadata(Resource):

    """
        The Metadata class will present users with the applicaitons build information.
        This will allow users to identify which version (and commit) of the service is running.
        This is achieved by serving the build.json which is generated during CI.
    """

    def get(self):

        build_file_path = pkg_resources.resource_filename('app', 'build.txt')

        if os.path.isfile(build_file_path):
            try:
                file = open(build_file_path, 'r')
            except (OSError, IOError) as e:
                return {"IOError encountered when trying to open metadata file."}, 500

            try:
                properties = dict(line.rstrip().split("=") for line in file)
                return properties
            except Exception as e:
                return {"Error encountered reading metadata file"} , 500

