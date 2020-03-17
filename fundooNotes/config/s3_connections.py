import logging
import boto3
from botocore.exceptions import ClientError

s3_client = boto3.client('s3')


class BotoService:

    def __init__(self):
        self.s3 = boto3.client('s3')

    def create_bucket(self, bucket_name, region=None):
        try:
            s3_client = boto3.client('s3', region_name=region)  # call s3 clint object
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
        except ClientError as e:
            logging.error(e)
            return False  # True if the referenced bucket, otherwise False
        return True

    def bucket_exist(self, bucket_name):
        s3 = boto3.resource('s3')
        print(s3.buckets.all)
        bucket = s3.Bucket(bucket_name) in s3.buckets.all()
        if bucket:
            return True
        else:
            return False

    def delete_bucket(self, bucket_name):
        try:
            s3_client.delete_bucket(Bucket=bucket_name)  # bucket_name: string
        except ClientError as e:
            logging.error(e)
            return False  # True if the referenced bucket was deleted, otherwise False
        return True

    def list_bucket_objects(self, bucket_name):
        # Retrieve the list of bucket objects
        try:
            response = s3_client.list_objects_v2(Bucket=bucket_name)
        except ClientError as e:
            # AllAccessDisabled error == bucket not found
            logging.error(e)
            return None
        return response['Contents']

    def delete_object(self, bucket_name, object_name):
        try:
            self.s3.delete_object(Bucket=bucket_name, Key=object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def upload_files(self, bucket_name, upload_file, file_name):
        try:
            s3_client.upload_file(upload_file, bucket_name, Key=file_name, ExtraArgs={
                'ACL': 'private'})
        except ClientError as e:
            logging.error(e)
            return False
        return True
