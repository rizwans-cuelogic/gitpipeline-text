env.DEPLOYMENT_LOCATION= "/home/rushikesh/janzati/CICD/"

pipeline{

    agent any 
    stages{
        stage('integration'){
            steps{
                sh '''#!/bin/bash -xe
                    sudo chmod 777 /home/rushikesh/janzati/CICD/ 
                    sudo cp -r . /home/rushikesh/janzati/CICD/
                    cd /home/rushikesh/janzati/CICD/
                    sudo virtualenv -p python3 myenv
                    source test/bin/activate
                    pip3 install -r requirements.txt
                    python3 manage.py migrate
                '''
                
            }
        }
        stage('deployment'){
            steps{
                sh "./app_run.sh"
            }

        }
    
    }

}