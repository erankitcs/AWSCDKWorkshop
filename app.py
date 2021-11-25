#!/usr/bin/env python3

from aws_cdk import core

from awscdk_workshop.awscdk_workshop_stack import AwscdkWorkshopStack


app = core.App()
AwscdkWorkshopStack(app, "awscdk-workshop")

app.synth()
