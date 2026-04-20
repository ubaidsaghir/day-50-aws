import boto3

s3 = boto3.client(
    's3',
    aws_access_key_id='AKIAVRUVVWHJGG6IUDOR',
    aws_secret_access_key='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'
)

response = s3.list_buckets()

for bucket in response['Buckets']:
    print(bucket['Name'])