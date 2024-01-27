from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_lambda_destinations as destinations,
    aws_sns_subscriptions as subscriptions
)
from constructs import Construct

class AwsLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        destination_queue = sqs.Queue(self, "DestinationQueue")
        trigger_sns = sns.Topic(self, "TriggerSns")
        my_lambda = _lambda.Function(
            self, 'MyLambda',
            runtime=_lambda.Runtime.PYTHON_3_11,
            code=_lambda.Code.from_asset('lambda_code'),
            handler='lambda_1.handler',
            on_success=destinations.SqsDestination(destination_queue),
            reserved_concurrent_executions=3
        )

        my_lambda.add_alias("Live", provisioned_concurrent_executions=2)
        trigger_sns.add_subscription(subscriptions.LambdaSubscription(my_lambda))