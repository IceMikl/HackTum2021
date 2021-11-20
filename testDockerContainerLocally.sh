#!/bin/bash
sudo docker container stop hacktum_image_container
sudo docker rm hacktum_image_container

sudo docker build -t hacktum_image .
sudo docker create --name hacktum_image_container --publish 8050:8050 hacktum_image

sudo docker start hacktum_image_container --interactive


# sudo docker build -t elegance.azurecr.io/hacktum_image_container:latest .
# sudo docker start elegance.azurecr.io/hacktum_image_container:latest --interactive
# docker login elegance.azurecr.io
# Username: elegance
# Password: y3/p6ynoK1VRYvba712=PdHartgkrDuQ
# docker push elegance.azurecr.io/hacktum_image_container:latest