[![Build Status](https://travis-ci.org/michaelgriffithssurefire/ops-challenge.svg?branch=master)](https://travis-ci.org/michaelgriffithssurefire/ops-challenge)

# MYOB ops challenge

This repository contains the code and documentation for my submission of the MYOB operations technical test (see https://github.com/MYOB-Technology/ops-technical-test)

This test was very fun to do and the open ended style of the specification was challenging as i needed to select technologies that could work everywhere as well as being careful that i didn't go too far out of scope.

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
This repository integrates with TravisCI and the code is built, tested, contianerised and pushed to a public docker repository with each push to the master branch.

# Assumptions

An assumption was made that the submitted artifact does not need to handle a large scale production workload but should be in a state that allows it to be consistently reviewed and tested.
The flask web server utilised in ops-challenge is not recommended for production use but can still be used for a production deployment when paired with Nginx or Apache using a WSGI configuration.

# Technology Used

Python - ops-challenge is written in Python 3.6

Flask_restful and Flask - Flask was used as a restful service framework and http server. Flask was quite useful as it comes with a test client built in and handles the management of API routes.

Travis CI - I selected Travs CI for the CI service as it is mentioned in the specification for the challenge and is also used by most of MYOB's open source projects. I was completely unfamiliar with Travis before this challenge and was very impressed with how simple the service is to set up and use.

Docker - Docker satisfied the condition that the application be packaged as a deployable artifact with dependencies enclosed.

# To run the app locally 


## Docker - (pulls the container from docker hub 323MB) and runs it.

```
docker run -d -p 8080:8080 werfcoder/ops-challenge:latest  
```

## Python (3.6)
*The script in the projects run/ directory named run_with_python.sh will perform the same tasks below.*

If you have other python related projects on your system making a virualenv is recommended.
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
python test_api.py
```

# Deployment

how can this app be deployed?


