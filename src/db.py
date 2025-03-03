import mysql.connector
from dotenv import load_dotenv, find_dotenv
import os

# This system environment variable `api_environment` can be set to differentiate env configs
env_file = ".env"
if os.getenv('api_environment', 'dev'):
    env_file += f".{os.getenv('api_environment', 'dev')}"

load_dotenv(find_dotenv(filename=env_file))
# hostname = os.getenv('db_host')

# MySQL connection
def db_connect():
    return mysql.connector.connect(
        host=os.getenv('db_host'),
        user=os.getenv('db_username'),
        password=os.getenv('db_password'),
        database=os.getenv('db_name')
    )

"""
Improvements:
- manage the database credentials using saltstack or k8s secrets for different environments
"""
