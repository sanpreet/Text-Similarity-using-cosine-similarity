# Text-Similarity-using-cosine-similarity  

## What is special in this code  
This code is compiled with class based structure. Salient features of this code includes following points
<ol>
  <li> Class based code is made.</li>
  <li> Functions are made inside the class to find the text similalrity</li>
  <li> Object is created and it calls the function to find text based similarity</li>
  </ol>  

## Dockerfile for this project  

I have created the docker file for this project so that user can run the code without the need to install the requirements in their system and process becomes more easy.Let me explain the docker file for your reference.   
```
FROM ubuntu:16.04: This is the base image on which I will run the python code. You may choose different tags which are mentioned. Check different tags from this link https://hub.docker.com/_/ubuntu
``` 
```
RUN apt-get update: apt is package management system and update is used to download package information     
from all configured sources
```
```
RUN apt-get install -y python3-pip python3-dev build-essential: This command is used to install pip for python3.  
python3-dev contains the header files you need to build Python extensions.  
The build-essentials package is a reference for all the packages needed to compile a Debian package.  
It generally includes the GCC/g++ compilers and libraries and some other utilities.  
Remember when each RUN commands is executed, a container is allocated.
```  
```  
WORKDIR /Text_Similarity: This will create a directory inside the container where one will run the image.
```
```
COPY . /Text_Similarity: This will copy all the files of your project in the newly created folder in the container
```
```
RUN pip3 install -r requirements.txt: Run the dependencies which are needed for this project.  
One can find the list of dependencies in the file requirements.txt which one can find in this repository. 
```
```
CMD [ "python3", "./Text_Similarity.py" ]: This command is used to run the file which contains code.  
User donot need to do any thing. All the things are done while writing the Dockerfile.
```  

## How to build the docker image  
Once you have written the Dockerfile (YOU can find here also. Please write the file name exactly same as Dockerfile), you need to create the docker image. To create the docker image, please proceed with the below step  
```
docker build -t **name_of_image** .
```
## How to push the image to the docker-hub  
To push the image to the docker-hub. Firstly create an account on docker hub. If you donot know, I am adding the link. Please go to it and create the account. https://hub.docker.com/signup?next=%2F%3Fref%3Dlogin. Once account is created, please create the respository name inside it and follows the below steps to push the image to the docker-hub. One can create either public or private repository.  
```
Step 1: Tag the image before pushing it.  
docker tag image_id **Yourdocker-hub-username/repository_name:commit**
Step 2: Push to this repsoitory  
docker push **Yourdocker-hub-username/repository_name:commit**  
```
Note: TO find the image tag just run the command in you terminal docker images. I believe all the readers have installed docker in their system before proceedings to these steps. If you face any problem, please see the below image.  

**command**: docker images and see the output as below  

![SCREENSHOT1_docker_images](https://user-images.githubusercontent.com/3431730/62416593-48baed80-b65b-11e9-8e07-6b799480907a.png)  
Let us also see how the image pushed to docker hub look likes  

![Screen_Shot_2_docker_hub](https://user-images.githubusercontent.com/3431730/62416610-8d468900-b65b-11e9-867e-80a0b3c24a2b.png)

## How to run this program without Dockerfile 

Since this program is written in python so to run this code, please run the below command in terminal  

```
python/python3 Text_Similarity.py   
```  

## How to run project using docker  
To run the project using the concept of docker, first it is needed to pull the image which is pushed in the docker hub. To pull this image the command remains same for all as I have made my repository public in the docker hub. Please execute the below command  

```
docker pull sanpreetai/text_similarity_nlp:first_commit  
```
You will see get the image in your system. Please note that you must have docker installed in your system. To get more grip of this command please see the below screeenshot.  

![docker_pull](https://user-images.githubusercontent.com/3431730/62418532-7ff3c380-b688-11e9-8120-fa48ea0104df.png)  

Now you have successfully pulled the image from my docker-hub. It is time to run the image. To run the image please execute the below command.    
```
docker run -it sanpreetai/text_similarity_nlp:first_commit
```
Please see the screenshot for more details.  

![Output](https://user-images.githubusercontent.com/3431730/62418544-e678e180-b688-11e9-9727-23f0ec672490.png)  

Happy Coding!!!
