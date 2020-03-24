#!/bin/sh
export GLUE_DATA_DIR=$1
echo "Run video glue"
docker-compose up
echo "Clean up the containers"
docker-compose rm -f
echo "Clean up the image"
docker rmi video-glue_video-glue
