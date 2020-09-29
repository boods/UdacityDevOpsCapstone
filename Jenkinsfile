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
        stage('Linting python code')
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
                            dockerImage.push() 
                        }
                    }
                }
            } 
        }

        stage('Deployment') {
            steps {
                dir("eks") {
                    script {
                        kubectl apply -f skills.yaml
                        kubectl apply -f skills-service.yaml
                    }
                }
            }
        }        

        stage('Rolling Deployment') {
            steps {
                script {
                    kubectl rollout restart deployment/skills-webserver
                }
            }
        }
    }
}