from aws_cdk import (
    Stack,
    aws_ec2 as ec2
)
from constructs import Construct

class AwsVpcStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(
            self, "my_vpc",
            ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16"),
            enable_dns_support=True,
            enable_dns_hostnames=True,
            max_azs=3,
            subnet_configuration=[ 
                { "cidrMask": 24, "name": "ingress", "subnetType": ec2.SubnetType.PUBLIC},
                { "cidrMask": 24, "name": "application", "subnetType": ec2.SubnetType.PRIVATE_WITH_EGRESS},
                { "cidrMask": 28, "name": "rds", "subnetType": ec2.SubnetType.PRIVATE_ISOLATED} ],
            vpc_name="my_vpc_01",
            )

        
