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
        stage('Build and upload docker')
        {
            steps {
                dir("skills") {
                    node {
                        def customImage = docker.build("capstone-skills:${env.BUILD_ID}")
                        customImage.push('latest')
                    }
                }
            }
        }
    }
}