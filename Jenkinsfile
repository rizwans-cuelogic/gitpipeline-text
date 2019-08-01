env.DEPLOYMENT_LOCATION= "/home/rushikesh/janzati/CICD/"

pipeline{

    agent any 
    stages{
        stage('integration'){
            steps{
                sh '''#!/bin/bash
                    sudo cp . ${env.DEPLOYMENT_LOCATION}
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