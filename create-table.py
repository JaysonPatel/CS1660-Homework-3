import boto3

# establish connection to dynamodb
dyndb = boto3.resource('dynamodb', region_name='us-west-2', aws_access_key_id='key', aws_secret_access_key='key')

try:
    table = dyndb.create_table(
        TableName='Experiments',
        KeySchema=[
        {
            'AttributeName': 'PartitionKey',
            'KeyType': 'HASH'
        },
        # {
        #     'AttributeName': 'RowKey',
        #     'KeyType': 'RANGE'
        # }
        ],
        AttributeDefinitions=[
        {
            'AttributeName': 'PartitionKey',
            'AttributeType': 'S'
        },
        # {
        #     'AttributeName': 'RowKey',
        #     'AttributeType': 'S'
        # },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

# if there is an exception, the table may already exist. if so...
except Exception as e:
    print (e)

    table = dyndb.Table("Experiments")

table.meta.client.get_waiter('table_exists').wait(TableName='Experiments')
print(table.item_count)