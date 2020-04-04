# 
# Author 2019 RocketML
#


import boto3
import json


def aws_comprehend():
    comprehend = boto3.client(service_name='comprehend', region_name='us-west-2')
    text = 'Accelerate your data science work with RocketML'
    
    jsonvalue = json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'),sort_keys=True, indent=4)
    
    decoded_hand = json.loads(jsonvalue)
    
    return decoded_hand['Entities'];


def test_aws_comprehend():
    value = aws_comprehend()
    decoded_hand = value
    
    org_name = decoded_hand[0]['Text']
    
    ent_type = decoded_hand[0]['Type']
    
    assert org_name == 'RocketML'
    assert ent_type == 'ORGANIZATION'
    
test_aws_comprehend()
