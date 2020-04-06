#
# @author  RocketML
#

import boto3
import os.path
import sys
import configparser


def read_config():
    config = configparser.ConfigParser()
    config_file_path = 'config.txt'
    config.read(config_file_path)
    return config

def download_content(bucket_name,file_name):
    s3_client = boto3.client('s3')
    response = s3_client.download_file(bucket_name, file_name, file_name)
    return response;

def test_aws_s3():

    config = read_config()

    bucket_name = config.get('s3_bucket_attached', 'bucket_name')
    file_name = config.get('s3_bucket_attached', 'file_name')

    download_content(bucket_name,file_name)
    is_file = os.path.isfile(file_name)

    assert is_file == True

test_aws_s3()
