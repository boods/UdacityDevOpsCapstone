# UdacityDevOpsCapstone
Capstone for Udacity Cloud DevOps

## Git Repo
https://github.com/boods/UdacityDevOpsCapstone

## Planning

I'm interested in playing the violin, and have been thinking about building an application for tracking practice progress. 
This project will setup a CI/CD pipeline for the first component of that application - a very basic python webapi, built using flask, to 
return a list of skills that can be practiced.

The target environment for deployments will comprise a VPN with two public subnets, an EKS cluster and nodegroup, and two bastion hosts (one in each subnet)

The pipeline will work as follows: 
1. Code will be checked into a github repo
2. A Jenkins server, running on an EC2 will monitor changes in the repo, and trigger builds
3. Jenkins will download the latest source
4. Jenkins will run pylint on the python code, and hadolint on the dockerfile
5. Jenkins will run the python unit tests
6. On successful linting, the Jenkins will build a docker image and push it to dockerhub, with the 'latest' tag
7. Finally, jenkins will perform a rolling update on the kubernetes cluster

The following diagram depicts the typical pipline flow: 
![alt text](https://github.com/boods/UdacityDevOpsCapstone/tree/master/docs/UdacityDevOpsCapstone.jpeg "Planning")

## Soure Code

The repo consists for the following: 
* infrastructure - AWS cloudformation templates for setting up the target environment, and bash scripts to create, update and delete the environment
* skills - the python application (skills.py), Makefile, DockerFile, and requirements.txt (detailing python library dependencies)
* skills/tests - python unit tests (test_skills.py)
* skills.yaml - kubernetes manifest for the skills webserver
* *skills-service.yaml - kubernetes manifest for the kubernetes load balancer

## Proving the pipline


### Linting

Make a breaking change to the python code and check it into github: 
![alt text](https://github.com/boods/UdacityDevOpsCapstone/tree/master/docs/1_breaking_python_change.png "Breaking Python Change")

Confirm that the build fails on the pylint step: 
![alt text](https://github.com/boods/UdacityDevOpsCapstone/tree/master/docs/2_build_failure_pylint.png "Failing pylint")

Fix the python error, but make a breaking change to the dockerfile and check that into git hub: 
![alt text](https://github.com/boods/UdacityDevOpsCapstone/tree/master/docs/3_breaking_dockerfile_change.png "Breaking dockerfile")

Confirm that the build is still failing, this time on the hadolint step: 
![alt text](https://github.com/boods/UdacityDevOpsCapstone/tree/master/docs/4_build_failure_hadolint.png "Failing hadolint")

Fix the dockerfile issue, commit the change and confirm that the linting is successful
![alt text](https://github.com/boods/UdacityDevOpsCapstone/tree/master/docs/5_successful_linting.png "Successful linting")

And full deployment is working: 
![alt text](https://github.com/boods/UdacityDevOpsCapstone/tree/master/docs/6_rolling_deployment.png "Successful deployment")


### Rolling Deployment

View the output with curl prior to deployment: 
![alt text](https://github.com/boods/UdacityDevOpsCapstone/tree/master/docs/7_curl_output.png "Output before deployment")

Make a small change to the skills.py to publish a new skill, and commit the change: 
![alt text](https://github.com/boods/UdacityDevOpsCapstone/tree/master/docs/8_code_change.png "Change code and commit")

Confirm the rolling deployment is performed by Jenkins:
![alt text](https://github.com/boods/UdacityDevOpsCapstone/tree/master/docs/9_rolling_deployment.png "Rolling Deployment in Jenkin")

Confirm the output with curl after deployment - notice the additional skill appearing: 
![alt text](https://github.com/boods/UdacityDevOpsCapstone/tree/master/docs/10_output_after_deployment.png "Output after deployment")

Perform a test where an EC2 instance in the cluster is taken offline, and a replacement instance started: 
![alt text](https://github.com/boods/UdacityDevOpsCapstone/tree/master/docs/11_auto_scaling.png "Auto scaling ECs")
