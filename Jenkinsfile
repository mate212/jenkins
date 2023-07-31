pipeline {
    agent {
        node {
            label 'docker-agent-python'
        }
    }
    triggers {
        pollSCM '* * * * *'
    }

    stages {
        stage('Build') {
            steps {
                sh '''
                cd app
                pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Testing .....'
                sh '''
                cd app
                python3 test.py
                python3 test.py --name=Name
                '''
            }
        }

        stage('Deliver') {
            steps {
                echo 'Delivering ....'
                sh '''
                echo "Delivering steps to be implemented"
                '''
            }
        }
    }
}
