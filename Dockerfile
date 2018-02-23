FROM python:3.6

MAINTAINER "Michael Griffiths" <michaelgriffithsaus@gmail.com>

ENV LAST_UPDATED 2018-02-23
ENV INSTALL_DIR = /usr/src/app

# Update packages and clean any un-needed packages, files or dependancies
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get clean -y && \
    apt-get purge -y && \
    apt-get autoclean -y && \
    apt-get autoremove -y

RUN mkdir -p usr/src/app

COPY app/ $INSTALL_DIR/

WORKDIR $INSTALL_DIR

RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8080" ]