pipeline {
    agent any
    stages {
        stage('Setup and activate python venv for skills') {
            steps {
                dir("skills") {
                    sh """
                        ls -la
                        make setup
                    """
                }
            }
        }
        stage('Install dependencies')
        {
            steps {
                dir("skills") {
                    sh """
                        ls -la
                        . .skills/bin/activate
                        make install
                    """
                }
            }
        }
        stage('Linting python code and dockerfile')
        {
            steps {
                dir("skills") {
                    sh """
                        . .skills/bin/activate
                        make lint
                    """
                }
            }
        }
        stage('Running unit tests')
        {
            steps {
                dir("skills") {
                    sh """
                        . .skills/bin/activate
                        make test
                    """
                }
            }
        }
        stage('Build the docker image') {
            steps {
                dir("skills") {
                    script { 
                        dockerImage = docker.build "youngphillip/capstone-skills:$BUILD_NUMBER" 
                        docker.withRegistry( '', 'dockerhub' ) { 
                            dockerImage.push( "latest" ) 
                        }
                    }
                }
            } 
        }
        stage('Rolling Deployment') {
            steps {
                withAWS(region: 'us-west-2', credentials: 'aws-static') {
                    sh """
                        kubectl apply -f skills.yaml
                        kubectl apply -f skills-service.yaml
                        kubectl rollout restart deployment/skills-webserver
                    """
                }
            }
        }        
    }
}