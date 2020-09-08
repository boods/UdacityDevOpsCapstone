pipeline {
    agent any
    stages {
        stage('Setup and activate python venv for skills') {
            steps {
                dir("skills") {
                    sh 'ls -la'
                    sh 'make setup'
                    sh 'source .skills/bin/activate'
                }
            }
        }
        stage('Install dependencies')
        {
            steps {
                dir("skills") {
                    sh 'make install'
                }
            }
        }
        stage('Linting python code')
        {
            steps {
                dir("skills") {
                    sh 'make lint'
                }
            }
        }
        stage('Running unit tests')
        {
            steps {
                dir("skills") {
                    sh 'make test'
                }
            }
        }
    }
}