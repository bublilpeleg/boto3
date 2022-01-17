import boto3
import datetime

session = boto3.session.Session(profile_name='root')
iam_con_re = session.resource(service_name='iam')

# get details of any iam user

iam_user_obj = iam_con_re.User("boto3")
print(iam_user_obj)
# print(iam_user_obj.user_name, iam_user_obj.user_id, iam_user_obj.arn, iam_user_obj.create_date.strftime("%y-%m-%d"))

# for iam_user_obj in iam_con_re.users.all():
#     print(iam_user_obj)
#     print(iam_user_obj.user_name, iam_user_obj.user_id, iam_user_obj.arn, iam_user_obj.create_date.strftime("%y-%m-%d"))

