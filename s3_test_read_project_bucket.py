import os.path
import boto3
import sys
import configparser

def read_config():
    config = configparser.ConfigParser()
    config_file_path = 'config.txt'
    config.read(config_file_path)
    return config


def download_content(remote_path):
    s3_client = boto3.client('s3')
    response = s3_client.download_file('rmlprojectsbucket',remote_path+'/copy.txt','downloaded.txt')
    return response;

def test_init_():
    config = read_config()

    project_bucket = config.get('s3_bucket_project', 'bucket_name')

    response = download_content(project_bucket)

    is_file = os.path.isfile('downloaded.txt')

    assert is_file == True

test_init_()