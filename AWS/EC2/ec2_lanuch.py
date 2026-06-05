import boto3
import time


REGION = "ap-south-1"
KEY_NAME = "my-key-boto3"
SECURITY_GROUP_NAME = "my-boto3-sg"


ec2 = boto3.client("ec2", region_name=REGION)
ssm = boto3.client("ssm", region_name=REGION)


print("Creating key pair...")

key_pair = ec2.create_key_pair(KeyName=KEY_NAME)

private_key = key_pair["KeyMaterial"]

with open(f"{KEY_NAME}.pem", "w") as file:
    file.write(private_key)

print(f"Saved key to {KEY_NAME}.pem")


vpcs = ec2.describe_vpcs()

vpc_id = vpcs["Vpcs"][0]["VpcId"]

print("Using VPC:", vpc_id)


print("Creating security group...")

sg = ec2.create_security_group(
    GroupName=SECURITY_GROUP_NAME,
    Description="Security group created using boto3",
    VpcId=vpc_id,
)


sg_id = sg["GroupId"]

print("Security Group ID:", sg_id)


ec2.authorize_security_group_ingress(
    GroupId=sg_id,
    IpPermissions=[
        {
            "IpProtocol": "tcp",
            "FromPort": 22,
            "ToPort": 22,
            "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
        }
    ],
)

print("Enabled SSH access")


ami_id = "ami-009be0edec0817ffd"

print("AMI ID:", ami_id)


print("Launching EC2 instance...")


response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType="t3.micro",
    MinCount=1,
    MaxCount=1,
    KeyName=KEY_NAME,
    SecurityGroupIds=[sg_id],
)

instance_id = response["Instances"][0]["InstanceId"]

print("Instance ID:", instance_id)


print("Waiting for instance to start...")

waiter = ec2.get_waiter("instance_running")
waiter.wait(InstanceIds=[instance_id])

print("Instance is running")


instance_info = ec2.describe_instances(InstanceIds=[instance_id])

public_ip = instance_info["Reservations"][0]["Instances"][0]["PublicIpAddress"]

print("Public IP:", public_ip)

print("\nSSH COMMAND:")
print(f"ssh -i {KEY_NAME}.pem ec2-user@{public_ip}")
