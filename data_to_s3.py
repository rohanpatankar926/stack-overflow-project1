from s3_sync import S3Sync
import os


class DataDumpS3:
    def __init__(self,file_path):
        self.file_path=file_path
        self.bucket_name="stack-overflow-bucket1"

    def dump_data(self):
        for file in os.listdir(self.file_path):
            if file.endswith(".xml"):
                data_dir=os.path.join(os.getcwd(),self.file_path)
                s3_uri=f"s3://{self.bucket_name}/stack_overflow_data"
                S3Sync.local_to_s3(data_dir,s3_uri)
            else:
                return "Only xml files are allowed"

if __name__=="__main__":
    DataDumpS3("data").dump_data()
