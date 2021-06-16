FROM python:3.7.9
LABEL maintainer="Alan Kwok"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python", "app.py" ]
