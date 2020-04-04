#
# @author  RocketML
#

import boto3
import os.path


def download_content():
    s3_client = boto3.client('s3')
    response = s3_client.download_file('rmlcontent', 'credit_card_03.png', 'credit_card_03.png')
    return response;

def test_aws_s3():
    download_content()
    is_file = os.path.isfile('credit_card_03.png')

    assert is_file == True

test_aws_s3()
