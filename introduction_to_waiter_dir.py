import time
import boto3

aws_con = boto3.session.Session(profile_name='root')
ec2_con_re = aws_con.resource(service_name='ec2', region_name='us-east-1')
ec2_con_cli = aws_con.client(service_name='ec2', region_name='us-east-1')

# my_inst_ob = ec2_con_re.Instance('i-0ca78f03fb2d705d9')
# print("Starting given instance...")
# my_inst_ob.start()
# my_inst_ob.wait_until_running()
# print("Now your instance is up and running ")

# =======================================================

# print("starting ec2 instance......")
# ec2_con_cli.start_instances(InstanceIds=['i-0ca78f03fb2d705d9'])
# waiter = ec2_con_cli.get_waiter('instance_running')
# waiter.wait(InstanceIds=['i-0ca78f03fb2d705d9'])
# print("now your ec2 instance is running")

# =======================================================

# my_inst_ob = ec2_con_re.Instance('i-0ca78f03fb2d705d9')
# print("Starting given instance...")
# my_inst_ob.start()
# waiter = ec2_con_cli.get_waiter('instance_running')
# waiter.wait(InstanceIds=['i-0ca78f03fb2d705d9'])
# print("now your ec2 instance is running")


# =======================================================