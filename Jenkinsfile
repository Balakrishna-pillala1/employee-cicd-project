pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t employee-app:v1 .'
            }
        }

        stage('List Docker Images') {
            steps {
                bat 'docker images'
            }
        }

    }
}