# postgres-connect.py
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Copyright (c) RocketML
#------------------------------------------------------------------------------

import psycopg2
import boto3
import base64
import requests
import json
import configparser

def connect_postgres(arn,db_host):

    try:

        session = boto3.session.Session()
        client = session.client('secretsmanager','us-west-2')

        response = client.get_secret_value(SecretId=arn)
        data = json.loads(response['SecretString'])

        connection = psycopg2.connect(user = data['username'],
                                      password = data['password'],
                                      host = db_host,
                                      port = "5432",
                                      database = "postgres")
        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        #print ( connection.get_dsn_parameters(),"\n")

        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        return len(record)

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            #print("PostgreSQL connection is closed")


def read_config():
    config = configparser.ConfigParser()
    config_file_path = 'config.txt'
    config.read(config_file_path)
    return config

def test_postgres_connect():
    config = read_config()

    run_rds_test_scripts = config.get('rds_config', 'run_rds_test_scripts')

    postgres_arn = config.get('postgres', 'postgres_arn')
    postgres_host = config.get('postgres', 'postgres_host')

    if run_rds_test_scripts == 'true':
        record = connect_postgres(postgres_arn,postgres_host)
        assert 1 == record
    else:
        print('db connectivity test is disabled')


test_postgres_connect()


