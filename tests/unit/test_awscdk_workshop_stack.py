from aws_cdk import (
        core,
        assertions
    )

from awscdk_workshop.awscdk_workshop_stack import AwscdkWorkshopStack


def test_sqs_queue_created():
    app = core.App()
    stack = AwscdkWorkshopStack(app, "awscdk-workshop")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_sns_topic_created():
    app = core.App()
    stack = AwscdkWorkshopStack(app, "awscdk-workshop")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
