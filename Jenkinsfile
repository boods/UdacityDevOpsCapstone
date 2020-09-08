pipeline {
    agent any
    stages {
        stage('Setup and activate python venv for skills') {
            steps {
                echo 'cd skills'
                sh 'cd skills'

                echo 'Run: make setup'
                sh 'make setup'
                
                echo 'Run: source .skills/bin/activate'
                sh 'source .skills/bin/activate'
            }
        }
        stage('Install dependencies')
        {
            steps {
                echo 'Run: make install'
                sh 'make install'
            }
        }
        stage('Linting python code')
        {
            steps {
                echo 'Run: make lint'
                sh 'make lint'
            }
        }
        stage('Running unit tests')
        {
            steps {
                echo 'Run: make test'
                sh 'make test'
            }
        }
    }
}