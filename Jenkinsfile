pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh '''
                    pwd
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    ls -ltr
                    python scripts/test.py
                '''
            }
        }
    }
}