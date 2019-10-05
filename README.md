# Una implementacion de K-means++
El notebook (y el módulo) puede correrse de dos maneras, utilizando anaconda o creando una imagen de Docker utilizando el Dockerfile que se encuentra en este repositorio. A continuación explicitamos cada una de ellas.
## Utilizando Anaconda
Para correrlo utilizando Anaconda sera necesario crear un enviroment basado en python 3.7. Ademas serán necesarias las librerias con las siguientes versiones:
* scikit-learn 0.21.2
* numpy 1.16.4 
* pandas 0.24.2

## Utilizando Docker
Para correr este notebook (y el modulo), se deberá crear una nueva imagen a partir del Dockerfile que se encuentra en este repositorio.\
Nota: El Dockerfile fue creado a partir de la imagen provista por el repositorio oficial de jupyter (jupyter/scipy-notebook).\
Encontrandonos en la direccion donde descargamos este Dockerfile, ejecutamos los siguientes comandos (siempre y cuando estemos utilizando alguna distribución de Linux).

`sudo docker build -t my_image .`

De esta manera creamos una imagen de Docker (llamada my_image) usando el Dockerfile en cuestion, podemos chequear la existencia de la misma, ejecutando:

`sudo docker images`

Una vez que tenemos la imagen en nuestro equipo, creamos un conteiner a partir de ella con el siguiente comando

`sudo docker run -p 8888:8888 my_image:latest`

Por ultimo copiar en nuestro navegador la dirección que se nos mostrará.
