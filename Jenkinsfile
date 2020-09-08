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
                        source .skills/bin/activate
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
                        source .skills/bin/activate
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
                        source .skills/bin/activate
                        make test
                    """
                }
            }
        }
    }
}