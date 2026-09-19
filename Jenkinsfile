pipeline {

    agent any


    stages {

       stage("Code clone"){
            steps{
                sh "whoami"
            clone("https://github.com/")
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
                docker compose down || true
                docker compose up -d
                '''
            }
        }
    }
}
