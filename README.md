# HackTum2021
HackTum project for Zeiss challenge.



### Build and push Docker container manually
Commands to build and push a Docker container with the application to the Azure Container Registry.
~~~
- sudo docker build -t elegance.azurecr.io/hacktum_image_container:latest .
- sudo docker start elegance.azurecr.io/hacktum_image_container:latest --interactive
- docker login elegance.azurecr.io
- Username: elegance
- Password: y3/p6ynoK1VRYvba712=PdHartgkrDuQ
- docker push elegance.azurecr.io/hacktum_image_container:latest
~~~