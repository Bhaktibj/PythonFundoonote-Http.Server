# import logging
# import boto3
# from botocore.exceptions import ClientError
# from setting import AWS_S3
#
# s3_client = boto3.client('s3')
# region = AWS_S3['region']  # get s3 bucket region
#
#
# class BotoService:
#     """ This class is used for create, delete s3 bucket and upload image or file in s3 also get object from s3"""
#
#     @staticmethod
#     def create_bucket(bucket_name, region=None):
#         """ This method is used to create the s3 bucket """
#         try:
#             s3_client = boto3.client('s3', region_name=region)  # call s3 client object
#             location = {'LocationConstraint': region}  # location
#             s3_client.create_bucket(Bucket=bucket_name,
#                                     CreateBucketConfiguration=location)  # create s3 bucket
#         except ClientError as e:
#             logging.error(e)
#             return False  # True if the referenced bucket, otherwise False
#         return True  # if bucket is created
#
#     @staticmethod
#     def bucket_exist(bucket_name):
#         """ This method is used for check bucket is exist or not"""
#         s3 = boto3.resource('s3')  # create boto3 resource object
#         bucket = s3.Bucket(bucket_name) in s3.buckets.all()  # Check bucket in s3_bucket_all or not
#         if bucket:  # if bucket return True
#             return True
#         else:
#             return False  # false
#
#     @staticmethod
#     def delete_bucket(bucket_name):
#         """ This method is used for to delete the bucket"""
#         try:
#             s3_client.delete_bucket(Bucket=bucket_name)  # bucket_name: string
#         except ClientError as e:
#             logging.error(e)
#             return False  # if given bucket is not deleted or does not exist False
#         return True  # True if given bucket is deleted
#
#     @staticmethod
#     def list_bucket_objects(bucket_name):
#         """ This  method is used to retrieve list of bucket object """
#         try:
#             response = s3_client.list_objects_v2(Bucket=bucket_name)
#         except ClientError as e:
#             # access desabled  bucket not found error
#             logging.error(e)
#             return None  # or if no objects return None
#         return response['Contents']  # return objects
#
#     @staticmethod
#     def delete_object(bucket_name, object_name):
#         """ This method is used for delete the object from s3  bucket """
#         try:
#             s3_client.delete_object(Bucket=bucket_name, Key=object_name)  # delete objects from bucket
#         except ClientError as e:
#             logging.error(e)
#             return False  # if no objects return false
#         return True  # if deleted return True
#
#     @staticmethod
#     def upload_files(bucket_name, upload_file, file_name):
#         """ This method is used to upload the image or file in bucket"""
#         try:
#             s3_client.upload_file(upload_file, bucket_name, Key=file_name, ExtraArgs={
#                 'ACL': 'private'})  # upload the image
#         except ClientError as e:
#             logging.error(e)
#             return False  # if bucket or image is none it retuns  False
#         return True  # if image is upload retunrs True
