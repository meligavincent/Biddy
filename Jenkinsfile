pipeline {
    agent any

    environment {
        DOCKER_IMAGE_DJANGO = 'dummy-django-image:latest'
        DOCKER_IMAGE_RASA = 'dummy-rasa-image:latest'
        COMPOSE_FILE = 'docker-compose.yml'
        EC2_HOST = 'dummy-ec2-instance-pain'
    }

    stages {

        stage('Checkout Biddy') {
            steps {
                echo 'Cloning the Biddy repository...'
                dir('Biddy') { // Clone Biddy into a subfolder named Biddy
                    git branch: 'main', credentialsId: 'biddy', url: 'https://github.com/meligavincent/Biddy.git'
                }
            }
        }

        stage('Checkout BiddyBot') {
            steps {
                echo 'Cloning the BiddyBot repository...'
                dir('BiddyBot') { // Clone BiddyBot into a subfolder named BiddyBot
                    git branch: 'main', credentialsId: 'BiddyBot', url: 'https://github.com/meligavincent/BiddyBot.git'
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                echo 'Step: Building Docker Images for Django and Rasa...'
                sh 'sudo docker compose up -d --build'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Step: Running Unit Tests for Django...'
                echo 'Step: Running Unit Tests for Rasa...'
            }
        }

        stage('Push Docker Images to Registry') {
            steps {
                echo 'Step: Pushing Docker Images to DockerHub or another registry...'
            }
        }

        stage('Deploy to EC2') {
            steps {
                echo 'Step: Deploying to EC2 instance via SSH...'
                echo "Step: Deploying Docker Compose file ${COMPOSE_FILE} on ${EC2_HOST}..."
            }
        }
    }

    post {
        always {
            echo 'Step: Cleaning up resources...'
        }

        success {
            echo 'Step: CI/CD pipeline completed successfully.'
        }

        failure {
            echo 'Step: CI/CD pipeline failed.'
        }
    }
}
