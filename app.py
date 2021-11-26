#!/usr/bin/env python3

from aws_cdk import core

from awscdk_workshop.awscdk_workshop_stack import AwscdkWorkshopStack
from awscdk_workshop.pipeline_stack import WorkshopPipelineStack

app = core.App()
#AwscdkWorkshopStack(app, "awscdk-workshop")
WorkshopPipelineStack(app, "WorkshopPipelineStack")

app.synth()
