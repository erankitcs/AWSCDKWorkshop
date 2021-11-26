
from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as apigw
)
from .hitcounter import HitCounter
from cdk_dynamo_table_view import TableViewer

class AwscdkWorkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime = _lambda.Runtime.PYTHON_3_7,
            code  = _lambda.Code.from_asset('lambda'),
            handler = 'hello.handler',
        )
        hello_with_counter = HitCounter(
            self, 'HelloHiCounter',
            downstream=my_lambda
        )
        myapi = apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=hello_with_counter._handler,
        )
        table_view = TableViewer(
            self, 'ViewHitCounter',
            table=hello_with_counter.table,
            title='HitCounterView'
        )
