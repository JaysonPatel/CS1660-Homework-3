import csv
import boto3

# establish connection to s3 account
s3 = boto3.resource('s3', aws_access_key_id ='key', aws_secret_access_key='key')

# establish connection to table
dyndb = boto3.resource('dynamodb', region_name='us-west-2', aws_access_key_id='key', aws_secret_access_key='key')
table = dyndb.Table("Experiments")

with open(r'C:\Users\Jayson\PycharmProjects\AWSHomework\assets\experiments.csv', 'rt', ) as csvfile:

    csvf = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(csvf)
    for item in csvf:
        print(item)
        body = open(r'C:\Users\Jayson\PycharmProjects\AWSHomework\assets\\'+item[4], 'rb')
        s3.Object('jrp134-cs1660-h3-bucket', item[4]).put(Body=body )
        md = s3.Object('jrp134-cs1660-h3-bucket', item[4]).Acl().put(ACL='public-read')

        url = " https://s3-us-west-2.amazonaws.com/jrp134-cs1660-h3-bucket/"+item[4]
        metadata_item = {'PartitionKey': item[0], 'Temp': item[1], 'Conductivity' : item[2], 'Concentration' : item[3], 'url':url}
        try:
            table.put_item(Item=metadata_item)
        except:
            print("item may already be there or another failure")
