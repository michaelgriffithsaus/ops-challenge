[![Build Status](https://travis-ci.org/michaelgriffithssurefire/ops-challenge.svg?branch=master)](https://travis-ci.org/michaelgriffithssurefire/ops-challenge)

# MYOB ops challenge

This repository contains the code and documentation for my submission of the MYOB operations technical test (see https://github.com/MYOB-Technology/ops-technical-test)

This test was very fun to do and the openended-ness of the specification was challenging as i needed to select technologies that could work everywhere as well as being careful that i didn't go too far out of scope.

# Assumptions



# The app

The application is a simple REST api service that responds on the following endpoints.

/
/health (applicaiton health check)
/metadata (build properties and application info)

# Design Choices 

how was it built and why?

# Technology Used

what tech was used and why?


# Development



# To run the app locally 

## Docker Run (pulls the container from docker hub 323MB)


## (Docker Compose)

```
git clone https://github.com/michaelgriffithssurefire/ops-challenge.git
cd ops-challenge
docker-compose up -d
```

## (python 3.6)

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


