#Deriving the latest base image
FROM python:latest

# Any working directory can be chosen as per choice like '/' or '/home' etc
WORKDIR /myapp

#to COPY the remote file at working directory in container
COPY . .

RUN pip install boto3 flask awscli

#CMD instruction should be used to run the software

EXPOSE 5000
RUN chmod -R 777 awsconfig.sh
CMD ["./awsconfig.sh"]