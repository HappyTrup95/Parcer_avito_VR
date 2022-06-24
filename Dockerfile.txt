FROM python
LABEL maintainer="neon19011995@gmail.com"
RUN apt-get update
RUN sudo apt-get install -y python3 && sudo apt-get install -y python3-pip 
RUN pip install selenium && pip install requests
COPY Parser_YAMareket /usr/local/bin/
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

CMD [ "python", "Unitiled-2.py" ]
