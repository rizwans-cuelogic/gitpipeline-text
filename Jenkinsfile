env.DEPLOYMENT_LOCATION= "/home/rushikesh/janzati/CICD/"

pipeline{

    agent any 
    stages{
        stage('integration'){
            steps{
                sh '''#!/bin/bash
                    virtualenv -p python3 myenv
                    source test/bin/activate
                    pip install -r requirements.txt
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