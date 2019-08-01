pipeline{

    agent any 
    stages{
    if(env.BRANCH_NAME=='development'){
        stage('integration'){
            steps{
                sh "ls "
            }
        }
        stage('deployment'){
            steps{
                input("Do you want to proceed?")
            }

        }
    }
    
    }

}