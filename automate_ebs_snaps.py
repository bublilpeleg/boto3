import boto3
from pprint import pprint

session = boto3.session.Session(profile_name='root')
ec2_client = session.client(service_name='ec2', region_name='us-east-1')
list_of_volids = []
f_prod_bkp = {'Name': 'tag:Prod', 'Values': ['backup']}
# pprint(ec2_client.describe_volumes()['Volumes'])
# for each_vol in ec2_client.describe_volumes(Filters=[f_prod_bkp])['Volumes']:
#     list_of_volid.append(each_vol['VolumeId'])
paginator = ec2_client.get_paginator('describe_volumes')
for each_page in paginator.paginate(Filters=[f_prod_bkp]):
    for each_vol in each_page['Volumes']:
        list_of_volids.append(each_vol['VolumeId'])
print("The list of volid are: ", list_of_volids)

for each_volid in list_of_volids:
    print('Taking snap of {}'.format(each_volid))
    response = ec2_client.create_snapshot(
        Description='Taking snap with lambda and cw',
        VolumeId=each_volid,
        TagSpecifications=[
            {
                'ResourceType': 'snapshot',
                'Tags': [
                    {
                        'Key': 'Delete-on',
                        'Value': '90'
                    }
                ]
            }
        ]
    )
    pprint(response)
