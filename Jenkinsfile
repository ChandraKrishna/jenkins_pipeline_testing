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
                sh 'python3 scripts/test.py'
            }
        }
    }
}