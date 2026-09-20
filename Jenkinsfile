pipeline {

    agent any


    stages {

      stage("Code Clone"){
            steps{
               script{
                   clone("https://github.com/Atharva731/Flask--App-Noteshub.git", "master")
               }
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
