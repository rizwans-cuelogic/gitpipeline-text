def getGitBranchName() {
    return scm.branches[0].name
}
pipeline{

    agent any 
    stages{
        stage('integration'){
            steps{
                 echo "THis is git branch ${getGitBranchName()}"
            }
        }
        stage('deployment'){
            steps{
                input("Do you want to proceed?")
            }

        }
    
    }

}