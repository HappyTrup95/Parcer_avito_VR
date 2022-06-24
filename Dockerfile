FROM ubuntu:latest
LABEL maintainer="neon19011995@gmail.com"

RUN apt-get update
RUN apt-get install -y python3 
RUN apt-get install -y python3-pip 
RUN pip install selenium 
RUN pip install requests

COPY ./ /Parser_YAMareket

CMD  ["python", "Untitled-2.py"]
 