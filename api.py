from flask import Flask,Response
import boto3
from xml.etree.ElementTree import tostring,fromstring,parse

s3=boto3.client("s3",aws_access_key_id="AKIA3RJ56UA2XCPUTO5A",aws_secret_access_key="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")

app=Flask(__name__)

@app.route("/")
def index():
    return "Server is up and running"

def get_data_from_s3(bucket_name,key):
    response=s3.get_object(Bucket=bucket_name,Key=key)
    data=response["Body"].read().decode("utf-8")
    return data

@app.route("/xml_data")
def get_data():
    xml_data=get_data_from_s3("stack-overflow-bucket1","stack_overflow_data/data.xml")
    root=fromstring(xml_data)
    xml_string=tostring(root,encoding="unicode")
    return Response(xml_string,mimetype="text/xml")


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)