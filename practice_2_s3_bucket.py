import boto3
from botocore.exceptions import NoCredentialsError, ClientError

s3 = boto3.client('s3')

file_name='spotify.csv'
bucket_name='ubaid-s3-storage-demo'
s3_file_name = 'uploads/data.csv'


try:
    s3.upload_file(file_name, bucket_name, s3_file_name)
    print("File Upload Successfully")
    
except FileNotFoundError:
    print("File not found")
    
except NoCredentialsError:
    print("Credentials not available")
    
except ClientError as e:
    print(f"AWS Error: {e}")            