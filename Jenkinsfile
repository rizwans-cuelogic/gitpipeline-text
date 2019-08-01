env.DEPLOYMENT_LOCATION= "/home/rushikesh/janzati/CICD/"

pipeline{

    agent any 
    stages{
        stage('integration'){
            steps{
                bash '''#!/bin/bash
                    virtualenv -p python3 myenv
                    source test/bin/activate
                    pip install -r requirements.txt
                    python manage.py migrate
                '''
                
            }
        }
        stage('deployment'){
            steps{
                sh "python manage.py runserver 0.0.0.0:8000"
            }

        }
    
    }

}