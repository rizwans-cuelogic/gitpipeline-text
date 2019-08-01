pipeline{

    agent any 
    stages{

        stage('One'){
            steps{
                ls
            }
        }
        stage('Two'){
            steps{
                input("Do you want to proceed?")
            }

        }
        stage('Three'){

                when{
                    not{
                        branch "development"
                    }

                }
                steps{
                    echo "hello"
                }

        }

    }

}