pipeline {

    agent any

    stages {

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
