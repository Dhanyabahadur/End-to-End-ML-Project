# End-to-End-ML-Project


```bash
conda create -n mlproj python=3.8 -y
```


```bash
conda activate mlproj 
```


```bash
pip install -r requirements.txt
```

```bash
python app.py
```

```bash
Now open up your local host 0.0.0.0:8080
```

# AWS-CI CD-Deployment-with-Github-Actions


## 1. Login to AWS console.

## 2. Create IAM user for deployment

```bash
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
```

## 3. Create ECR repo to store/save docker image
```bash
- Save the URI: 975050189648.dkr.ecr.us-east-1.amazonaws.com/mlproject
```

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:

```bash
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

## 6. Configure EC2 as self-hosted runner:

```bash
setting>actions>runner>new self hosted runner> choose os> then run command one by one
```

## 7. Setup github secrets:

```bash
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app
```



## Workflows

1. update config.yaml
2. update schema.yaml
3. update params.yaml
4. update the entity
5. update the configuration manager in src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the app.py