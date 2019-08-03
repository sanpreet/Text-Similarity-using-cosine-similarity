FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python3-pip python3-dev build-essential
WORKDIR /Text_Similarity
COPY . /Text_Similarity
RUN pip3 install -r requirements.txt
CMD [ "python3", "./Text_Similarity.py" ]

