env.DEPLOYMENT_LOCATION= "/home/rushikesh/janzati/CICD/"

pipeline{

    agent any 
    stages{
        stage('integration'){
            steps{
                sh "sudo docker build -t images/injazati_rest_file ."
            }
        }
        stage('deployment'){
            steps{
                sh "sudo docker run -d -e 8000:8000 --network='host' images/injazati_rest_file"
            }

        }
    
    }

}