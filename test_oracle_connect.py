#------------------------------------------------------------------------------
# oracle-connect.py (Section 1.2 and 1.3)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Copyright (c) 2017, 2018, Oracle and/or its affiliates. All rights reserved.
#------------------------------------------------------------------------------

from __future__ import print_function

import cx_Oracle
import boto3
import base64
import requests
import json
import configparser

def connect_oracle(arn,db_host):
    session = boto3.session.Session()
    client = session.client('secretsmanager','us-west-2')

    response = client.get_secret_value(SecretId=arn)
    data = json.loads(response['SecretString'])

    dsn_tns = cx_Oracle.makedsn(db_host, '1521','orcl')

    conn = cx_Oracle.connect(data['username'],data['password'],dsn_tns)

    return conn

def read_config():
    config = configparser.ConfigParser()
    config_file_path = 'config.txt'
    config.read(config_file_path)
    return config

def test_oracle_connect():
    config = read_config()

    run_rds_test_scripts = config.get('rds_config', 'run_rds_test_scripts')

    oracle_arn = config.get('oracle', 'oracle_arn')
    oracle_host = config.get('oracle', 'oracle_host')

    if run_rds_test_scripts == 'true':
        conn = connect_oracle(oracle_arn,oracle_host)

        cur = conn.cursor()
        executed = cur.execute('select count(*) from dba_tables')
        res = cur.fetchmany(numRows=1)

        row_number = len(res)

        assert row_number == 1
        cur.close()
        conn.close()
    else:
        print('no run')


test_oracle_connect()

