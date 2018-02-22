#init routes
from flask import Flask
from flask_restful import Resource, Api

#Import API Routes
from resources import helloworld
from resources import health
from resources import metadata

app = Flask('app')
api = Api(app, catch_all_404s=True)

#config to be moved to seperate dir
app.config['SECRET_KEY'] = 'random'
app.debug = True

#Add API Routes
api.add_resource(helloworld.HelloWorld, '/')
api.add_resource(health.Health, '/health')
api.add_resource(metadata.Metadata, '/metadata')

if __name__ == '__main__':
    app.run(debug=True)


