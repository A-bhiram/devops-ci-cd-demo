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
    }
}
