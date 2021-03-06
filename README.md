[![Build Status](https://travis-ci.org/michaelgriffithsaus/ops-challenge.svg?branch=master)](https://travis-ci.org/michaelgriffithsaus/ops-challenge)

# MYOB ops challenge

This repository contains the code and documentation for my submission of the MYOB operations technical test (see https://github.com/MYOB-Technology/ops-technical-test)

This test was very fun to do and the open ended style of the specification was challenging as I needed to select technologies that could work everywhere as well as being careful that I didn't go too far out of scope in the limited timeframe.

The application is a simple REST api service that responds on the following endpoints.

**/**
```
curl localhost:8080
{
    "hello": "world"
}
```

**/health** (application health check)
```
curl localhost:8080/health
{
    "status": "UP"
}
```

**/metadata** (build properties and application info)
```
curl localhost:8080/metadata
{
    "app_description": "Pre-interview technical test",
    "travis_build_number": "22",
    "git_sha": "0358d6bd1f1c9f1ae2a276101712beda90f1836f",
    "triggered_by": "push",
    "build_date": "20180224_1259"
}
```
This repository integrates with TravisCI and the code is built, tested, containerised and pushed to a public docker repository with each push to the master branch.

Build properties are generated during the CI process and mapped into the Docker container.

# Assumptions

An assumption was made that the submitted artifact does not need to handle a large scale production workload but should be in a state that allows it to be consistently reviewed and tested.
The flask web server utilised in ops-challenge is not recommended for production use but can still be used for a production deployment when paired with Nginx or Apache using a WSGI configuration.

# Technology Used

Python - ops-challenge is written in Python 3.6

Flask_restful and Flask - Flask was used as a restful service framework and http server. Flask was quite useful as it comes with a test client built in and handles the management of API routes.

Travis CI - I selected Travis CI for the CI service as it is mentioned in the specification for the challenge and is also used by most of MYOB's open source projects. I was completely unfamiliar with Travis before this challenge and was very impressed with how simple the service is to set up and use.

Docker - Docker satisfied the condition that the application be packaged as a deployable artifact with dependencies enclosed.

# To run the app locally 


## Docker - (pulls the container from docker hub 323MB) and runs it.

```
docker run -d -p 8080:8080 werfcoder/ops-challenge:latest  
```

## Python (3.6)

If you have other python related projects on your system making a virtualenv is recommended.
```
$virtualenv ~/ops-challenge-virt
```

Activate the virtual environment:
```
source ~/ops-challenge-virt/bin/activate
```

Clone the repository and run the app
```
git clone https://github.com/michaelgriffithssurefire/ops-challenge.git
cd ops-challenge
pip install -r requirements.txt
python app/run.py
```

To run the tests

```
python app/test_api.py
```

# Reflections

There are several things I would like to improve with this project and fully intend to implement them in the future.

The default python 3.6 container is very large (323 MB) for such a small project and doesn't provide the best experience for the interviewer reviewing the application as they have to wait a minute or two for the container to pull before anything happens.
Given more time I would have reviewed more applicable container OS's or built my own base Python image with a much lighter footprint.

More error handling could be implemented especially around the metadata class. The metadata class could be protected better against erroneous formatting or characters in the build file.

Add more unit tests rather than just testing for sunny day scenarios.

Taking the flask application config out of run.py and instead importing the configuration from a /config directory.
This will allow the application to behave differently based on pre-defined environment variables.
For example if ENVIRONMENT=PROD load in config/PROD.txt on startup instead.

Running the project locally (not from docker) does not give you all of the build properties as the properties are populated and mapped into the container at build time.
This means there is a slight inconsistency between the raw code and the code in production which can lead to serious issues in larger projects.
The risk of this issue could be lessened by running an integration test in the CI process against the container as well which would ensure that the build properties generated by Travis don't break the application.

The artifact is not production ready and should be further configured with WSGI configuration or have gunicorn or nginx shipped as well. 
To manage this I would include relevant configuration in a separate config file in the application with switches for relevant deployment options and in a separate repository or CD tool manage the deployment of ops-challenge. 
