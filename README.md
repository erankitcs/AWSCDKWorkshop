
# Welcome to your CDK Python project!

## Feature 
1. Simple API built using AWS CDK Python.
2. Custom Construct feature of AWS CDK.
3. Uses of Pre-Built Construct Libraries.
4. Automated Testing and Validation of AWS CDK based Apps.
5. CDK Pipeline for Deployment of Apps and Validation.
## Architecture-
### Basic App with CDK Construct
![Alt text](images/hello-arch.png?raw=true "Basic App")
### Basic App with Imported CDK Construct
![Alt text](images/table-viewer.png?raw=true "Basic App")
### CI/CD Pipeline for CDK App
![Alt text](images/cdk-pipeline.JPG?raw=true "Basic App")
![Alt text](images/cdk-pipeline-1.JPG?raw=true "Basic App")

You should explore the contents of this project. It demonstrates a CDK app with an instance of a stack (`awscdk_workshop_stack`)
which contains an Amazon SQS queue that is subscribed to an Amazon SNS topic.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization process also creates
a virtualenv within this project, stored under the .venv directory.  To create the virtualenv
it assumes that there is a `python3` executable in your path with access to the `venv` package.
If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv
manually once the init process completes.

To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

You can now begin exploring the source code, contained in the hello directory.
There is also a very trivial test included that can be run like this:

```
$ pip install -r requirements-dev.txt
$ pytest
```

To add additional dependencies, for example other CDK libraries, just add to
your requirements.txt file and rerun the `pip install -r requirements.txt`
command.

## Tutorial  
See [this useful workshop](https://cdkworkshop.com/30-python.html) on working with the AWS CDK for Python projects.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation


Enjoy!
