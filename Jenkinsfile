pipeline {
    agent any

    environment {
        VENV = "/Users/gabrielodame/.jenkins/python-venv"
        PIP_CACHE = "/Users/gabrielodame/.jenkins/.pip-cache"
        DJANGO_SETTINGS_MODULE = "rduploadservice.settings"
        PYTHON = "/Users/gabrielodame/.jenkins/python-venv/bin/python"
        PYTHONPATH = "${WORKSPACE}/rduploadservice"
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

        stage('Debug Workspace') {
            steps {
                echo 'Inspecting workspace structure...'
                sh '''
                echo "Workspace structure:"
                ls -R ${WORKSPACE}
                '''
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                sh '''
                set -e
                if [ ! -d "/Users/gabrielodame/.jenkins/python-venv" ]; then
                    echo "Creating virtual environment..."
                    python3 -m venv /Users/gabrielodame/.jenkins/python-venv
                else
                    echo "Virtual environment already exists."
                fi
                /Users/gabrielodame/.jenkins/python-venv/bin/python -m pip install --upgrade pip setuptools wheel
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies from requirements.txt...'
                sh '''
                set -e
                /Users/gabrielodame/.jenkins/python-venv/bin/python -m pip install --no-cache-dir --cache-dir=/Users/gabrielodame/.jenkins/.pip-cache -r requirements.txt
                /Users/gabrielodame/.jenkins/python-venv/bin/python -m pip list
                '''
            }
        }

        stage('Run Migrations') {
            steps {
                echo 'Running Django migrations...'
                sh '''
                set -e
                /Users/gabrielodame/.jenkins/python-venv/bin/python ./rduploadservice/manage.py migrate --settings=${DJANGO_SETTINGS_MODULE}
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests with pytest...'
                sh '''
                set -e
                /Users/gabrielodame/.jenkins/python-venv/bin/python -m pytest --junitxml=test-results.xml
                '''
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }

        stage('Collect Static Files') {
            steps {
                echo 'Collecting static files for deployment...'
                sh '''
                set -e
                /Users/gabrielodame/.jenkins/python-venv/bin/python ./rduploadservice/manage.py collectstatic --noinput --settings=${DJANGO_SETTINGS_MODULE}
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
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
    }
}
