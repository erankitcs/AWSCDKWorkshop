
# Welcome to your CDK Python Advanced project!

## MultiRegion S3 Replication with KMS.

create a virtualenv on MacOS and Linux:

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

Get Account ID

```
$ export ACCOUNT_ID=$(aws sts get-caller-identity --output text --query Account)
```
Update your account ID into app.py file.

Bootstrapping

```
$ npx cdk bootstrap --cloudformation-execution-policies "arn:aws:iam::aws:policy/AdministratorAccess" aws://$ACCOUNT_ID/us-east-1 aws://$ACCOUNT_ID/us-east-2
```

Synth - Use * Any chars or  ? Single name pattern to match stacks. 
```
$ npx cdk synth Multi*
```

Deploy the App 

```
$ npx cdk deploy Multi*
```

Testing

Upload a file to the source bucket, and ensure that it is replicated to the target bucket. You can verify the S3 bucket settings as well, like versioning, default KMS CMK encryption, and the replication configuration.

Destroy the app

```
$ npx cdk destroy Multi*
```

