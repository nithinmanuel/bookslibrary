FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
# set up work directory
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/


# "python.pythonPath": "/bin/python3",
# here requirements.txt will have all softwares needed to add a new software
# add it in the requirement.txt and then do docker-compose down to down all 
# the running containers , later docker-compose up -d --build to rebuild the 
# image and contianer in this process the new requirement get installed during 
# the image build up  