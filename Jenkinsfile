pipeline {
    agent any
    stages {
        stage('Setup and activate python venv') {
            echo 'Run: make setup'
            sh 'make setup'
            
            echo 'Run: source .skills/bin/activate'
            sh 'source .skills/bin/activate'
        }
        stage('Install dependencies')
        {
            echo 'Run: make install'
            sh 'make install'
        }
        stage('Linting python code')
        {
            echo 'Run: make lint'
            sh 'make lint'
        }
        stage('Running unit tests')
        {
            echo 'Run: make test'
            sh 'make test'
        }
    }
}