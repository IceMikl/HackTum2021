#!/bin/bash
sudo docker build -t hacktum_image .
sudo docker container stop elegance.azurecr.io/hacktum_image_container:latest
sudo docker rm elegance.azurecr.io/hacktum_image_container:latest
sudo docker create --name elegance.azurecr.io/hacktum_image_container:latest --publish 8050:8050 hacktum_image
sudo docker start elegance.azurecr.io/hacktum_image_container:latest --interactive


# From the videos: https://www.youtube.com/watch?v=O5aXcmKc1HU
# sudo docker build -t elegance.azurecr.io/hacktum_image_container:latest .
# docker login elegance.azurecr.io
# Username: elegance
# Password: y3/p6ynoK1VRYvba712=PdHartgkrDuQ
# docker push elegance.azurecr.io/hacktum_image_container:latest