import boto3
import json

data = []

client = boto3.client('organizations')
response = client.list_accounts()

data = [{"{#Account_ID}":resp["Id"]} for resp in response['Accounts']]

data = {'data':data}
json_pre = json.dumps(data)
print (json_pre)
    
