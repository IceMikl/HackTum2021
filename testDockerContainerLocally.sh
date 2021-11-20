#!/bin/bash
sudo docker container stop hacktum_image_container
sudo docker rm hacktum_image_container
sudo docker build -t hacktum_image .
sudo docker create --name hacktum_image_container --publish 8050:8050 hacktum_image
sudo docker start hacktum_image_container --interactive