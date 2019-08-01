env.DEPLOYMENT_LOCATION= "/home/rushikesh/janzati/CICD/"

pipeline{

    agent any 
    stages{
        stage('integration'){
            steps{
                sh "ls"
                sh "cp -r . ${env.DEPLOYMENT_LOCATION}"
                sh "virtualenv test"
                sh "source test/bin/activate"
                sh "pip install -r requirements.txt"
                sh "python manage.py migrate"
            }
        }
        stage('deployment'){
            steps{
                sh "python manage.py runserver 0.0.0.0:8000"
            }

        }
    
    }

}