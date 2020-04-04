# COPYRIGHT:
#
# Copyright 2018-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.
#
#  modified by @RocketML
from __future__ import print_function

import time
import boto3
import random

def aws_transcribe():
    transcribe = boto3.client('transcribe', region_name='us-west-2')

    #response = transcribe.delete_transcription_job(
    #   TranscriptionJobName='test-transcribe_unit'
    #)

    job_name = str(random.randrange(10, 1000, 3))
    #job_uri = "https://S3 endpoint/test-transcribe/answer2.wav"

    job_uri="https://rmlaudio.s3-us-west-2.amazonaws.com/subfolder/example.wav"

    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat='wav',
        LanguageCode='en-US'

    )

    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
        print("Not ready yet...")
        time.sleep(5)
    print(status)

    return status;


def test_aws_transcribe():
    status = aws_transcribe();
    #print(status);
    job_status = status['TranscriptionJob']['TranscriptionJobStatus']
    job_name = status['TranscriptionJob']['TranscriptionJobName']
    media_sample_rate = status['TranscriptionJob']['MediaSampleRateHertz']

    assert job_status == 'COMPLETED'
    assert media_sample_rate == 16000

test_aws_transcribe()
