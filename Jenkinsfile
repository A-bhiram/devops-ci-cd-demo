pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/A-bhiram/devops-ci-cd-demo.git', branch: 'main'
            }
        }

        stage('Hello') {
            steps {
                echo '🎉 Hello, Jenkins pipeline is working!'
            }
        }

        stage('Install Dependencies') {
            steps {
sh 'pip install --break-system-packages -r requirements.txt'            }
        }

        stage('Lint') {
            steps {
                sh 'pylint *.py || true'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest || true'
            }
        }
    }
}
