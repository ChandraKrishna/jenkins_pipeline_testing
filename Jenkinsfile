pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                //
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
        stage('Deploy') {
            steps {
                //
            }
        }
    }
}