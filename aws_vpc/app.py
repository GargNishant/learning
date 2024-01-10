#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_vpc.aws_vpc_stack import AwsVpcStack


app = cdk.App()
vpc_stack = AwsVpcStack(app, "AwsVpcStack")
cdk.Tags.of(vpc_stack).add("application", "learning")

app.synth()
