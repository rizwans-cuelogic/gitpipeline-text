pipeline{

    agent any 
    stages{
        stage('integration'){
            steps{
                 echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL} on ${BRANCH_NAME}"
            }
        }
        stage('deployment'){
            steps{
                input("Do you want to proceed?")
            }

        }
    
    }

}