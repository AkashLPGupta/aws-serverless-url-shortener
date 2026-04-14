from aws_cdk import (
    Stack, aws_dynamodb as ddb, aws_lambda as lmb,
    aws_apigateway as apigw, aws_s3 as s3,
    RemovalPolicy, Duration
)
from constructs import Construct

class UrlShortenerStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # DynamoDB Table
        table = ddb.Table(self, 'UrlTable',
            table_name='url-shortener-table',
            partition_key=ddb.Attribute(
                name='shortCode', type=ddb.AttributeType.STRING),
            billing_mode=ddb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY
        )

        # Lambda Function
        fn = lmb.Function(self, 'UrlFunction',
            function_name='url-shortener-function',
            runtime=lmb.Runtime.PYTHON_3_11,
            handler='handler.lambda_handler',
            code=lmb.Code.from_asset('lambda'),
            timeout=Duration.seconds(10)
        )
        table.grant_read_write_data(fn)

        # API Gateway
        api = apigw.LambdaRestApi(self, 'UrlApi',
            handler=fn,
            rest_api_name='url-shortener-api',
            proxy=True
        )