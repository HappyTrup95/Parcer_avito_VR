FROM python:latest
LABEL maintainer="neon19011995@gmail.com"
WORKDIR /Parser_YAMareket
COPY ./ /Parser_YAMareket
RUN apt-get update  
RUN apt-get install -y python3 && apt-get install -y python3-pip && apt-get install -y wget 
RUN pip install selenium==4.2.0 && pip install requests && pip install webdriver-manager

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# set display port to avoid crash
ENV DISPLAY=:99

CMD ["python", "Untitled-2.py"]
 