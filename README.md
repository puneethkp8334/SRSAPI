#Assessment for SRS Business Soution

Tools & Solutions to use:  GIT,Dockers,K8, AWS, DB, JENKINS, Terraform, Microservices, Others

 

1)Use Public GITHUB store your demo Microservices web application code. At least have min 2 microservices in the application. (Can use GO or Python or JAVA)
2)RDBMS or any SQL DB Is must in your application your microservices access.
3)Build your Microservice based Demo Application using JENKINS when code commit triggered from GIT Repository.
4)Run few automated tests in JENKINS pipeline
5)Create Docker Image in the JENKINS pipeline and store it in AWS ECR or Docker hub
6)Build AWS EC2,RDS, ALB, CF and other resources needed to run your microservice application. Use Terraform or cloud formation to build the infrastructure VIA Jenkins.  Provision right IAM Roles and polices.
7)The microservice need to run in a Kubernetes based environment K8 or AWS EKS or others.
8)Once K8 Environment is up and running deploy the latest version of application into the K8 Cluster as PODS in a namespace – Use Jenkins + other available tools.
9)Demo scaling up and down of application PODS.
10)Demo your microservices application working via web URL.








Execute 
Step1: git clone https://github.com/puneethkp8334/SRS.git
step2:cd SRS
step3:docker-compose up --build 
step4:check docker running  docker ps command
  out put like this
CONTAINER ID   IMAGE       COMMAND                  CREATED          STATUS          PORTS                                                    NAMES
24242032ecbe   srs_app     "/bin/sh -c 'python …"   34 minutes ago   Up 38 seconds   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp                srs_app_1
5d9135b65e6d   mysql:5.7   "docker-entrypoint.s…"   4 days ago       Up 39 seconds   33060/tcp, 0.0.0.0:32000->3306/tcp, :::32000->3306/tcp   srs_db_1

step 5:open postman and enter the url get(change ip to your ip address)
       GET 3.111.23.173:5000/products
