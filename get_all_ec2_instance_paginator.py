import boto3

session = boto3.session.Session(profile_name='root')
ec2_cli = session.client('ec2')
paginator = ec2_cli.get_paginator('describe_instances')
for each_page in paginator.paginate():
    for res in each_page['Reservations']:
        for inst in res['Instances']:
            print(inst['InstanceId'])
