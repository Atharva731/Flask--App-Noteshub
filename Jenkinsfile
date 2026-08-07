pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh 'python -m pytest'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t noteshub:ci .'
            }
        }

    }
}
