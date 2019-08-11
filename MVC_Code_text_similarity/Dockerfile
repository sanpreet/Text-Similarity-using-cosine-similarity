FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python3-pip python3-dev build-essential
RUN apt-get install -y libssl-dev
WORKDIR /Text_Similarity
COPY . /Text_Similarity
RUN pip3 install -r requirements.txt
