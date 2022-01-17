import time
import boto3

aws_con = boto3.session.Session(profile_name='root')
ec2_con_re = aws_con.resource(service_name='ec2', region_name='us-east-1')
ec2_con_cli = aws_con.client(service_name='ec2', region_name='us-east-1')

my_inst_ob = ec2_con_re.Instance('i-0ca78f03fb2d705d9')
print("Starting given instance...")
my_inst_ob.start()

while True:
    my_inst_ob = ec2_con_re.Instance('i-0ca78f03fb2d705d9')
    print("The current status of ec2 is:", my_inst_ob.state['Name'])
    if my_inst_ob.state['Name'] == "running":
        break
    print("waiting to get  running state")
    time.sleep(5)

print("Now your instance is up and running ")
