import boto3

# establish connection to s3 account
s3 = boto3.resource('s3', aws_access_key_id ='key', aws_secret_access_key='key')

# create a bucket
try:
    s3.create_bucket(Bucket='jrp134-cs1660-h3-bucket', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})
except Exception as e:
    print(e)

# change bucket to public read
bucket = s3.Bucket("jrp134-cs1660-h3-bucket")
bucket.Acl().put(ACL='public-read')

