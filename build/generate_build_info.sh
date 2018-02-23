#!/usr/bin/env bash
# Written by Michael Griffiths
# This script will be ran by Travis after a successful build to generate the build information.

# Stop the script when an error occurs
set -o errexit

# Puts the script in debug mode (will print every line to stdout before each line executes)
#set -o xtrace

PROPERTIES_FILE='app/build.txt'

echo "build.travis_build_number=$TRAVIS_BUILD_NUMBER" >> $PROPERTIES_FILE
echo "build.description=Pre-interview technical test" >> $PROPERTIES_FILE
echo "build.git_sha=$TRAVIS_COMMIT" >> $PROPERTIES_FILE
echo "build.triggered_by=$TRAVIS_EVENT_TYPE" >> $PROPERTIES_FILE
echo "build.date=`date +%Y%m%d_%H%M`" >> $PROPERTIES_FILE

cat $PROPERTIES_FILE