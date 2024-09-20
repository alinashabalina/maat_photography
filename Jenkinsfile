pipeline {
    agent { docker { image 'python:3.8-alpine3.20' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}