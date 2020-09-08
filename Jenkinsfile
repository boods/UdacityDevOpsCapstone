pipeline {
    agent any
    stages {
        stage('Setup and activate python venv for skills') {
            steps {
                sh 'cd skills'
                sh 'make setup'
                sh 'source .skills/bin/activate'
            }
        }
        stage('Install dependencies')
        {
            steps {
                sh 'make install'
            }
        }
        stage('Linting python code')
        {
            steps {
                sh 'make lint'
            }
        }
        stage('Running unit tests')
        {
            steps {
                sh 'make test'
            }
        }
    }
}