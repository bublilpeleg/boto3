import boto3

session = boto3.session.Session(profile_name='root')
iam_cli = session.client('iam')
paginator = iam_cli.get_paginator('list_users')
for each_page in paginator.paginate():
    for each_user in each_page['Users']:
        print(each_user['UserName'])
