import boto3

# establish connection to s3 account
s3 = boto3.resource('s3', aws_access_key_id ='key', aws_secret_access_key='key')

# upload blobs to bucket
body = open('assets\exp1.csv', 'rb')
o = s3.Object('jrp134-cs1660-h3-bucket', 'exp1.csv').put(Body=body)
s3.Object('jrp134-cs1660-h3-bucket', 'exp1.csv').Acl().put(ACL='public-read')

body = open('assets\exp2.csv', 'rb')
o = s3.Object('jrp134-cs1660-h3-bucket', 'exp2.csv').put(Body=body)
s3.Object('jrp134-cs1660-h3-bucket', 'exp2.csv').Acl().put(ACL='public-read')

body = open('assets\exp3.csv', 'rb')
o = s3.Object('jrp134-cs1660-h3-bucket', 'exp3.csv').put(Body=body)
s3.Object('jrp134-cs1660-h3-bucket', 'exp3.csv').Acl().put(ACL='public-read')

body = open('assets\experiments.csv', 'rb')
o = s3.Object('jrp134-cs1660-h3-bucket', 'experiments.csv').put(Body=body)
s3.Object('jrp134-cs1660-h3-bucket', 'experiments.csv').Acl().put(ACL='public-read')
