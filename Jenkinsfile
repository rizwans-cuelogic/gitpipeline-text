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
                '''
                
            }
        }
        stage('deployment'){
            steps{
                sh "sudo docker build -t images/injazati_rest_file ."
                sh "sudo docker run -it -e 8000:8000 --network='host' images/injazati_rest_file"
            }

        }
    
    }

}