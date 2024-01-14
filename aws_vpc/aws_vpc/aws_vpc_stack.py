from aws_cdk import (
    Stack,
    aws_ec2 as ec2
)
from constructs import Construct

class AwsVpcStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # TODO: Attaching Transit Gateway to NAT Gateway for overlapping VPC

        self.vpc_1 = ec2.Vpc(
            self, "my_vpc_1",
            ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16"),
            enable_dns_support=True,
            enable_dns_hostnames=True,
            max_azs=1,
            subnet_configuration=[
                { "cidrMask": 28, "name": "S3", "subnetType": ec2.SubnetType.PRIVATE_ISOLATED}],
            vpc_name="my_vpc_01",
            )

        self.vpc_2 = ec2.Vpc(
            self, "my_vpc_2",
            ip_addresses=ec2.IpAddresses.cidr("192.168.0.0/24"), #192.168.0.0 - 192.168.0.255 = 256 IP
            enable_dns_support=True,
            enable_dns_hostnames=True,
            max_azs=1,
            subnet_configuration=[
                {"cidrMask": 25, "name": "S1", "subnetType": ec2.SubnetType.PRIVATE_ISOLATED},
            ]
        )

        self.tgw_1 = ec2.CfnTransitGateway(
            self, id="tgw_1",
            auto_accept_shared_attachments="enable",
            default_route_table_association="enable",
            default_route_table_propagation="enable"
        )

        self.tgw_attachment_1 = ec2.CfnTransitGatewayAttachment(
            self, id=f"tgw-1-vpc-1",
            transit_gateway_id=self.tgw_1.ref,
            vpc_id=self.vpc_1.vpc_id,
            subnet_ids=[subnet.subnet_id for subnet in self.vpc_1.isolated_subnets]
        )

        self.tgw_attachment_2 = ec2.CfnTransitGatewayAttachment(
            self, id=f"tgw-1-vpc-2",
            transit_gateway_id=self.tgw_1.ref,
            vpc_id=self.vpc_2.vpc_id,
            subnet_ids=[subnet.subnet_id for subnet in self.vpc_2.isolated_subnets]
        )
