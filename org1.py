import json
nested_dict = {
    'Accounts': [{
        'Id': '74634657346587',
        'Arn': 'arn:aws:organizations::sdgdfgdsf:account/o-bdsfhjjwmq6j/fdsfs',
        'Email': 'email',
        'Name': 'jfghgjhf',
        'Status': 'ACTIVE',
        'JoinedMethod': 'INVITED',
        "JoinedTimestamp": "2020-12-24 21:08:28.778000+05:30"
    },
    {
        'Id': '9991885327483709',
        'Arn': 'arn:aws:organizations::9991885327483709:account/o-bsfdskwmq6j/9991885327483709',
        'Email': 'aemail@gmail.com',
        'Name': 'Abdul',
        'Status': 'ACTIVE',
        'JoinedMethod': 'INVITED',
        "JoinedTimestamp": "2020-12-24 21:08:28.778000+05:30"
    }   
    ],
    'ResponseMetadata': {
        'RequestId': '4249344b-aff0-4a28-a0e2-3d47e4257aca',
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'x-amzn-requestid': '4249344b-aff0-4a28-a0e2-3d47e4257aca',
            'content-type': 'application/x-amz-json-1.1',
            'content-length': '251',
            'date': 'Wed, 06 Jan 2021 04:28:51 GMT'
        },
        'RetryAttempts': 0
    }
} 

del nested_dict["ResponseMetadata"] 

for l in nested_dict['Accounts']:
    for k in ["Arn", "Email","JoinedTimestamp"]:
        del l[k]

json_object = json.dumps(nested_dict, indent = 4)   
print(json_object)  

