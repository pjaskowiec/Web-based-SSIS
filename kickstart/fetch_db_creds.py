
# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/

import argparse
import boto3
from botocore.exceptions import ClientError
import json


def get_secret():

    secret_name = "student-app/db-local-creds"
    region_name = "eu-north-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    return get_secret_value_response['SecretString']


def format_secrets_to_env(secrets):
    formatted_string = ""
    for key, value in secrets.items():
        formatted_string += f'--env "{key}={value}" '
    return formatted_string


def format_secrets_to_build_args(secrets):
    formatted_string = ""
    for key, value in secrets.items():
        formatted_string += f'--build-arg {key}={value} '
    return formatted_string

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Optional app description')
    parser.add_argument(
        '--image-name', action='store', 
        required=True, type=str, help='The result image name.')
    parser.add_argument(
        '--tag', action='store', 
        required=True, type=str, help='The result image name.')
    parser.add_argument(
        '--build', action='store', type=bool, help='The result image name.')
    args = parser.parse_args()
    secrets = get_secret()
    if args.build:
        print(
            f"docker build --no-cache {format_secrets_to_build_args(json.loads(secrets))} -t {args.image_name}:{args.tag} .")
    else:
        print(
            f"docker run -it {format_secrets_to_env(json.loads(secrets))} {args.image_name}:{args.tag}")