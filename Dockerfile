FROM ubuntu:20.04

RUN apt update -y 
RUN apt install -y python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app
RUN pwd
RUN ls -la
RUN python3 --version

ENTRYPOINT [ "python3", "app.py" ]


