import os.path
import boto3
import sys

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
    uploaded = s3_client.upload_file(ab_file_path,'rmlprojectsbucket',upload_path+'/hello2.txt')
    return 1;

def test_init_():
    if len(sys.argv) != 2:
        print('pass in tracking uri')
    sys.exit(1)

    project_bucket = sys.argv[1]

    #project_bucket = "aatif.salehingmail/ProejctByAscw14pi"

    response = upload_file(project_bucket)

    assert 1 == response

test_init_()