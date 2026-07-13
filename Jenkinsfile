pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat 'cd'
            }
        }

        stage('Test') {
            steps {
                bat 'py scripts\\test.py'
            }
        }

        stage('Run JMeter') {
            steps {
                bat '"C:\\Users\\erkri\\Workspace\\JMeter_Jenkins\\5.6.3\\bin\\jmeter.bat" -n -t "C:\\Users\\erkri\\Workspace\\JMeter_Jenkins\\localhost.jmx" -l "C:\\Users\\erkri\\Workspace\\JMeter_Jenkins\\localhost_result.jtl"'
            }
        }
    }
}