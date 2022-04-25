# MyAwsProject

Routes

entrypoint of the project - http://127.0.0.1:5000/
it will render the simple html page with three navigation button from where we can navigate to create ec2 instance,some functionality, upload and download 
from already created s3 bucket

http://127.0.0.1:5000/createec2instance - 
it will render the createEc2.html page where we can provide the data and using those data we can create an ec2 instance by simply submiting the values
after submitting it will call the url http://127.0.0.1:5000/create which call the create function which will create the ec2 instnce on your aws account

http://127.0.0.1:5000/ec2Setting - 
navigate to this endpoint here you can get the public ip address of your instance, terminate and also stop the instances by just providing the instance id
all the function are implented in backend using boto3

http://127.0.0.1:5000/getinstance - 
after providing the instance id in the above endpoint this endpoint will navigate to another page and shows the ip address of your ec2 instance

http://127.0.0.1:5000/terminateinstance - 
after providing the instance id in the above endpoint this endpoint will navigate to another page and shows the terminated successfully message on the page
and your ec2 instance terminated 

http://127.0.0.1:5000/stopinstance - 
after providing the instance id in the above endpoint this endpoint will navigate to another page and shows the stopped successfully message on the page
and your ec2 instance stopped

http://127.0.0.1:5000/storage - 
it will navigate to the html page where you can upload the file from the computer to the s3 bucket which we hardcoded in the programme i.e in my case it 
is flaskdisk and you can also download the file from s3 bucket to your computer by just clicking on the name of the item listing on the browser

awsconfig.sh file -
this file is use to configure aws cli by providing the access_key, access_secret_key and region through enviornmental variable

Dockerfile - 
In this file we are copying whole folder to the WORKDIR which we created as /myapp and exposing 5000 port and running the bash file using CMD

How to Run - 
1 - we can run the python file using python3 app.py, it will run the file and your server will up and running

2 - We can also run the app.py using docker by making the image using this command
  docker build . -t <name>
  after creating image we have to create the container using the command
  sudo docker run -e x=<Access_key> -e y=<Access_secret_key> -e z=<region_name> -i -p 5000:5000  <image_name>
  after creating container again our server is up and running and we can access the above endpoints now

3 - pull the image from dockerhub
  command - docker pull himanshuinnogeek/awsproject:1.0
  this will create the image with name himanshuinnogeek/awsproject:1.0
  now we can create the container out of it and use the above endpoints for our usage.
 
