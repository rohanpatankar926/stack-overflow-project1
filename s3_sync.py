import os

class S3Sync:
    def local_to_s3(folder,aws_s3_bucket_url):
        command=f"aws s3 sync {folder} {aws_s3_bucket_url}"
        os.system(command=command)
    
    def s3_to_local(folder,aws_s3_bucket_url):
        command=f"aws s3 sync {aws_s3_bucket_url} {folder}"
        os.system(command=command)

