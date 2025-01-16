pipeline {
    agent any

    environment {
        VENV = "/Users/gabrielodame/.jenkins/venv" // Virtual environment path
        PIP_CACHE = "/Users/gabrielodame/.jenkins/.pip-cache" // pip cache
        DJANGO_SETTINGS_MODULE = "rduploadservice.settings" // Django settings module
        PYTHON = "/Users/gabrielodame/.jenkins/venv/bin/python" // Python in venv
        PYTHONPATH = "/Users/gabrielodame/.jenkins/workspace/rduploadservice" // Add project directory to PYTHONPATH
    }

    stages {
        stage('Initialize') {
            steps {
                echo 'Cleaning workspace and preparing environment...'
                cleanWs()
            }
        }

        stage('Checkout Code') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                sh '''
                python3 -m venv /Users/gabrielodame/.jenkins/venv
                source /Users/gabrielodame/.jenkins/venv/bin/activate
                /Users/gabrielodame/.jenkins/venv/bin/python -m pip install --upgrade pip setuptools wheel
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies from requirements.txt...'
                sh '''
                source /Users/gabrielodame/.jenkins/venv/bin/activate
                /Users/gabrielodame/.jenkins/venv/bin/python -m pip install --no-cache-dir --cache-dir=/Users/gabrielodame/.jenkins/.pip-cache -r requirements.txt
                /Users/gabrielodame/.jenkins/venv/bin/python -m pip list
                '''
            }
        }

        stage('Run Migrations') {
            steps {
                echo 'Running Django migrations...'
                sh '''
                source /Users/gabrielodame/.jenkins/venv/bin/activate
                /Users/gabrielodame/.jenkins/venv/bin/python ./rduploadservice/manage.py migrate --settings=rduploadservice.settings
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests with pytest...'
                sh '''
                source /Users/gabrielodame/.jenkins/venv/bin/activate
                /Users/gabrielodame/.jenkins/venv/bin/python -m pytest --junitxml=test-results.xml
                '''
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }

        stage('Static Files Collection') {
            steps {
                echo 'Collecting static files for deployment...'
                sh '''
                source /Users/gabrielodame/.jenkins/venv/bin/activate
                /Users/gabrielodame/.jenkins/venv/bin/python ./rduploadservice/manage.py collectstatic --noinput --settings=rduploadservice.settings
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh '''
                echo "Deploy step is a placeholder. Add deployment commands here."
                '''
            }
        }

        stage('Debug Environment') {
            steps {
                echo 'Debugging environment and permissions...'
                sh '''
                echo "Current user: $(whoami)"
                echo "Current directory: $(pwd)"
                ls -ld /Users/gabrielodame/.jenkins
                ls -ld /Users/gabrielodame/.jenkins/workspace
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
        always {
            echo 'Cleaning up virtual environment...'
            sh "rm -rf /Users/gabrielodame/.jenkins/venv" // Remove the virtual environment
            cleanWs()
        }
    }
}
