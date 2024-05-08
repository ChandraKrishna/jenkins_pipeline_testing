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
                script {
                    def pythonReturnValue = sh(script: 'python3 scripts/test.py', returnStdout: true)   
                    echo "Return Value from Python Script : ${pythonReturnValue}"                 
                }
            }
        }
    }
}