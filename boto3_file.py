import boto3
import os
def create_key_pair(keyName):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    key_pair = ec2_client.create_key_pair(KeyName=keyName)

    private_key = key_pair["KeyMaterial"]

    # write private key to file with 400 permissions
    with os.fdopen(os.open("/tmp/aws_ec2_key.pem", os.O_WRONLY | os.O_CREAT, 0o400), "w+") as handle:
        handle.write(private_key)


def create_instance(data):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    instances = ec2_client.run_instances(
        ImageId=data["imageId"],
        MinCount=int(data["minCount"]),
        MaxCount=int(data["maxCount"]),
        InstanceType=data["instanceType"],
        KeyName=data["keyName"]
    )
    print(instances["Instances"][0]["InstanceId"])


def get_public_ip(instance_id):
    """
    Function to get the public ip address of the EC2 instance
    """
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get("Reservations")

    for reservation in reservations:
        for instance in reservation['Instances']:
            return instance.get("PublicIpAddress")


def stop_instance(instance_id):
    """
    Function to stop the ec2 instance
    """
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    response = ec2_client.stop_instances(InstanceIds=[instance_id])
    print(response)


def terminate_instance(instance_id):
    """
    Function to terminate the ec2 instance
    """
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    response = ec2_client.terminate_instances(InstanceIds=[instance_id])
    print(response)


def upload_file(file_name, bucket):
    """
    Function to upload a file to an S3 bucket
    """
    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)

    return response


def download_file(file_name, bucket):
    """
    Function to download a given file from an S3 bucket
    """
    s3 = boto3.resource('s3')
    output = file_name
    s3.Bucket(bucket).download_file(file_name, output)

    return output

def list_files(bucket):
    """
    Function to list files in a given S3 bucket
    """
    s3 = boto3.client('s3')
    contents = []
    for item in s3.list_objects(Bucket="flaskdisk")['Contents']:
        contents.append(item)

    return contents