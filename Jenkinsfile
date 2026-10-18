
pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Checkout from GitHub') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Parvath0/student-registration-cicd.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t student-registration:1.0 .'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh '''
                    docker run --rm \
                      --network cicd-network \
                      -v "$WORKSPACE:/app" \
                      -w /app \
                      python:3.12-slim \
                      sh -c "pip install -q selenium && python tests/test_app.py"
                '''
            }
        }

        stage('Deploy Registration Form') {
            steps {
                sh '''
                    docker rm -f student-registration || true
                    docker run -d \
                      --name student-registration \
                      --network cicd-network \
                      -p 8081:80 \
                      student-registration:1.0
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the stage logs.'
        }
    }
}
