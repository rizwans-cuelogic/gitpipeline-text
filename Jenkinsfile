pipeline{

    agent any 
    stages{
        stage('integration'){
            steps{
                sh "ls"
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