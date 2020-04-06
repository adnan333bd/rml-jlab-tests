import os.path
import boto3
import sys

import configparser

def read_config():
    config = configparser.ConfigParser()
    config_file_path = 'config.txt'
    config.read(config_file_path)
    return config

def create_file():

    file = open("copy.txt", "w")
    file.write("Your text goes here")

    ab_file_path = os.getcwd() + "/" + file.name

    file.close()

    print(ab_file_path)
    return ab_file_path


def upload_file(upload_path):
    ab_file_path = create_file()
    s3_client = boto3.client('s3')
    uploaded = s3_client.upload_file(ab_file_path,'rmlprojectsbucket',upload_path+'/copy.txt')
    return 1;

def test_init_():

    config = read_config()
    project_bucket = config.get('s3_bucket_project', 'bucket_name')

    response = upload_file(project_bucket)

    assert 1 == response

test_init_()