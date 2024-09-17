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
                echo 'Cloning the repository...'
                git branch: 'main', credentialsId: 'fe933224-e6c6-461f-886b-3b5b46ba6305', url: 'https://github.com/meligavincent/Biddy.git'
            }
        }

        stage('Checkout BiddyBot') {
            steps {
                echo 'Cloning the repository...'
                git branch: 'main', credentialsId: '0936b05f-e2ae-4f84-806f-5b8aa88a8c5e', url: 'https://github.com/meligavincent/BiddyBot.git'
            }
        }

        stage('Prepare') {
            steps {
                echo 'Installing Docker Compose....'
                sh 'sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose'
                sh 'sudo chmod +x /usr/local/bin/docker-compose'
            }
        } 


        stage('Checkout') {
            steps {
                echo 'Step: Checking out the repository...'
            }
        }

        stage('Build Docker Images') {
            steps {
                echo 'Step: Building Docker Images for Django and Rasa...'
                sh 'sudo docker-compose build'

                sh 'sudo docker-compose up -d'

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
