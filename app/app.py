#init routes
from flask import Flask
from flask_restful import Resource, Api

#Import API Routes
from routes import helloworld
from routes import health
from routes import metadata

APP = Flask('app')
API = Api(APP, catch_all_404s=True)

#config to be moved to seperate dir
APP.config['SECRET_KEY'] = 'random'
APP.debug = True

#Add API Routes
API.add_resource(helloworld.HelloWorld, '/')
API.add_resource(health.Health, '/health')
API.add_resource(metadata.Metadata, '/metadata')

if __name__ == '__main__':
    APP.run()
