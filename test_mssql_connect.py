# mssql-connect.py
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Copyright (c) RocketML
#------------------------------------------------------------------------------

import pyodbc
import boto3
import base64
import requests
import json
import configparser


def connect_mssql(arn,host):
    session = boto3.session.Session()
    client = session.client('secretsmanager','us-west-2')

    response = client.get_secret_value(SecretId=arn)


    data = json.loads(response['SecretString'])

    server = host
    database = 'master'
    username = data['username']
    password = data['password']

    print ('user name : ' + data['username'])
    print ('user name : ' + data['password'])

    driver = sorted(pyodbc.drivers()).pop()

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    print(cnxn)

    #cursor = cnxn.cursor()

    return cnxn;

def read_config():
    config = configparser.ConfigParser()
    config_file_path = 'config.txt'
    config.read(config_file_path)
    return config

def test_mssql_connect():

    config = read_config()

    run_rds_test_scripts = config.get('rds_config', 'run_rds_test_scripts')

    mssql_arn = config.get('mssql', 'mssql_arn')
    mssql_host = config.get('mssql', 'mssql_host')

    if run_rds_test_scripts == 'true':
        cnxn = connect_mssql(mssql_arn,mssql_host)
        cursor = cnxn.cursor()
        cursor.execute ("SELECT DB_NAME()")
        row = cursor.fetchone()
        con = 'master' in row
        assert True == con
    else:
        print('no run')

test_mssql_connect()





