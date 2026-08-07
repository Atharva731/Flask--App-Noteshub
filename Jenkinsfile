pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }


        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                venv/bin/pip install --upgrade pip
                venv/bin/pip install -r requirements.txt
                '''
            }
        }


        stage('Test') {
            steps {
                sh '''
                venv/bin/python -m pytest
                '''
            }
        }


        stage('Docker Build') {
            steps {
                sh '''
                docker build -t noteshub:latest .
                '''
            }
        }


        stage('Deploy') {
            steps {
                sh '''
                docker stop noteshub-app || true
                docker rm noteshub-app || true

                docker run -d \
                --name noteshub-app \
                -p 5000:5000 \
                noteshub:latest
                '''
            }
        }

    }
}
