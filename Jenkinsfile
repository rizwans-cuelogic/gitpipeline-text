pipeline{
    environment {
        registry = "docker_hub_account/repository_name"
        registryCredential = 'dockerhub'
    }
    agent any 
    stages{
        stage('integration'){
            steps{
                bash '''#!/bin/bash
                    if [ ! -d venv ] ; then

                        virtualenv --python=python3 venv
                        fi
                        source venv/bin/activate
                        export PYTHONPATH="$PWD:$PYTHONPATH"

                        pip install pylint
                        ls .
                        cd repo
                        ### Need this because some strange control sequences when using default TERM=xterm
                        export TERM="linux"

                        ## || exit 0 because pylint only exits with 0 if everything is correct
                        pylint --rcfile=pylint.cfg $(find . -maxdepth 1 -name "*.py" -print) MYMODULE/ > pylint.log || exit 0          
                '''
            }
        }
        stage('deployment'){
            steps{
                sh "sudo docker build -t images/injazati_rest_file ."
                sh "sudo docker run -d -e 8000:8000 --network='host' images/injazati_rest_file"
            }

        }
    
    }

}