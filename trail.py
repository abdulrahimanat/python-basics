import logging
import os
import time
import boto3
S3_BUCKET="cf-abdul"

def lambda_handler(event, context):
    
    def _client(event, client_type):
        return boto3.client(client_type, region_name="us-east-1")
        
    organizations = _client(event, "organizations")  
    cloudtrail = _client(event, "cloudtrail")  
    try:
        enable_all_features_response = organizations.enable_all_features()

    except Exception as e:
        print(e)
    try:
        enable_aws_service_access_response = organizations.enable_aws_service_access(
            ServicePrincipal='cloudtrail.amazonaws.com'
            )
    except Exception as e:
        print(e)
