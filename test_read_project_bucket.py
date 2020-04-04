import os.path
import boto3
import sys

def download_content(remote_path):
    s3_client = boto3.client('s3')
    response = s3_client.download_file('rmlprojectsbucket', 'readme.txt', remote_path+'/readme.txt')
    return response;

def test_init_():

    if len(sys.argv) != 2:
        print('pass in tracking uri')
        sys.exit(1)

    project_bucket = sys.argv[1]

    #project_bucket = "aatif.salehingmail/ProejctByAscw14pi"

    response = download_content(project_bucket)

    is_file = os.path.isfile('readme.txt')

    assert is_file == True

test_init_()