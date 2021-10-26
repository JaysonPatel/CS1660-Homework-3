import csv
import boto3

# establish connection to s3 account
s3 = boto3.resource('s3', aws_access_key_id ='key', aws_secret_access_key='key')

# establish connection to table
dyndb = boto3.resource('dynamodb', region_name='us-west-2', aws_access_key_id='key', aws_secret_access_key='key')
table = dyndb.Table("Experiments")

response = table.get_item(Key={'PartitionKey': '3'})
item = response['Item']
print(item)

response