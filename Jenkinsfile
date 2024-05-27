pipeline {
    agent any
    triggers {
        cron('H/5 * * * *')
    }
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