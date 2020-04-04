#
# @author  RocketML
#
import boto3


def download_image_content():

    s3_client = boto3.client('s3')
    s3_client.download_file('rmlcontent', 'credit_card_03.png', 'credit_card_03.png')

def aws_textract():
    documentName = "credit_card_03.png"

    textract = boto3.client('textract',region_name='us-west-2')

    # Read document content
    with open(documentName, 'rb') as document:
        imageBytes = bytearray(document.read())

    # Call Amazon Textract
    response = textract.detect_document_text(Document={'Bytes': imageBytes})


    values = []

    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            print ('\033[94m' +  item["Text"] + '\033[0m')
            values.append(item["Text"])

    return values;


def test_aws_textract():
    download_image_content()
    extracted_result = aws_textract()
    print(extracted_result)

    print(extracted_result[0])

    assert extracted_result[0] == 'BED BATH &'
    assert extracted_result[1] == 'BEYOND'

    assert extracted_result[4] == 'VALID THRU 10/21'

    assert extracted_result[5] == 'Mastercard'
    assert extracted_result[6] == 'BB ANN BEYOND'

test_aws_textract()

