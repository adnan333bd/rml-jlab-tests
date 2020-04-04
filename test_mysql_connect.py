#------------------------------------------------------------------------------
# Copyright (c) RocketML
#------------------------------------------------------------------------------

import pymysql
import boto3
import configparser

def connect_mysql(arn,host):
    session = boto3.session.Session()
    client = session.client('secretsmanager','us-west-2')

    response = client.get_secret_value(SecretId=arn)

    data = json.loads(response['SecretString'])

    database = 'rmldb'
    username = data['username']
    password = data['password']

    print ('user name : ' + data['username'])
    print ('user name : ' +data['password'])

    # Open database connection
    db = pymysql.connect(host,username,password,database )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print ("Database version : %s " % data)

    execute_query = cursor.execute("SELECT id FROM rml_address LIMIT 1")

    result = cursor.fetchone()

    db.close()

    return execute_query

def read_config():
    config = configparser.ConfigParser()
    config_file_path = 'config.txt'
    config.read(config_file_path)
    return config

def test_mysql_connectivity():
    config = read_config()

    run_rds_test_scripts = config.get('rds_config', 'run_rds_test_scripts')

    mysql_arn = config.get('mysql', 'mysql_arn')
    mysql_host = config.get('mysql', 'mysql_host')

    if run_rds_test_scripts == 'true':
        query_executed = connect_mysql(mysql_arn,mysql_host)
        assert query_executed == 1
    else:
        print('no run')

test_mysql_connectivity()
