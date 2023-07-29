from flask import Flask,jsonify,Response
import boto3
import os


s3=boto3.client("s3",aws_access_key_id="",aws_secret_access_key="")


class S3Sync:
    def local_to_s3(folder,aws_s3_bucket_url):
        command=f"aws s3 sync {folder} {aws_s3_bucket_url}"
        os.system(command=command)
    
    def s3_to_local(folder,aws_s3_bucket_url):
        command=f"aws s3 sync {aws_s3_bucket_url} {folder}"
        os.system(command=command)

app=Flask(__name__)

@app.get("/get_data")
def get_data_from_s3(bucket_name,key):
    respose=s3.get_object(bucket_name,key)
    data=respose["Body"].read().decode("utf-8")
    return data


@app.get("/send_data")
def send_data_to_s3(file_path):
    for file in os.listdir(file_path):
        data_dir=os.path.join(os.getcwd(),file)
        s3_url=""
        S3Sync().local_to_s3(data_dir,s3_url)


@app.route("/")
def index():
    return "Server is up and running"

