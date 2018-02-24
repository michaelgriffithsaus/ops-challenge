#!/usr/bin/env bash
# Written by Michael Griffiths
# This script will be ran by Travis after a successful build to generate the build information.
# This build information will be mapped into the docker container at the end of the build.

# Stop the script when an error occurs
set -o errexit

# Puts the script in debug mode (will print every line to stdout before each line executes)
#set -o xtrace

PROPERTIES_FILE='app/build.txt'

echo "travis_build_number=$TRAVIS_BUILD_NUMBER" >> $PROPERTIES_FILE
echo "git_sha=$TRAVIS_COMMIT" >> $PROPERTIES_FILE
echo "triggered_by=$TRAVIS_EVENT_TYPE" >> $PROPERTIES_FILE
echo "build_date=`date +%Y%m%d_%H%M`" >> $PROPERTIES_FILE

cat $PROPERTIES_FILE