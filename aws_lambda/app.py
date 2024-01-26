#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_lambda.aws_lambda_stack import AwsLambdaStack


app = cdk.App()
AwsLambdaStack(app, "AwsLambdaStack")

app.synth()
