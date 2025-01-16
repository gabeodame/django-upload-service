pipeline {
    agent any

    environment {
        VENV = "/Users/gabrielodame/.jenkins/python-venv" // Virtual environment path
        PIP_CACHE = "/Users/gabrielodame/.jenkins/.pip-cache" // pip cache
        DJANGO_SETTINGS_MODULE = "rduploadservice.settings" // Django settings module
        PYTHON = "/Users/gabrielodame/.jenkins/python-venv/bin/python" // Python binary in virtual environment
        PYTHONPATH = "${WORKSPACE}/rduploadservice" // Add project directory to PYTHONPATH
    }

    stages {
        stage('Initialize') {
            steps {
                echo 'Cleaning workspace and preparing environment...'
                cleanWs()
            }
        }

        stage('Debug Python Environment') {
            steps {
                echo 'Checking Python 3.10 environment...'
                sh '''
                set -e
                echo "Python 3.10 version:"
                /usr/local/bin/python3.10 --version || { echo "Python 3.10 not found"; exit 1; }
                echo "Python 3.10 location:"
                which python3.10 || { echo "which command failed to find Python 3.10"; exit 1; }
                '''
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python virtual environment with Python 3.10...'
                sh '''
                set -e
                if [ ! -d "${VENV}" ]; then
                    echo "Creating virtual environment with Python 3.10..."
                    /usr/local/bin/python3.10 -m venv ${VENV} || { echo "Failed to create virtual environment"; exit 1; }
                else
                    echo "Virtual environment already exists."
                fi
                ${VENV}/bin/python -m pip install --upgrade pip setuptools wheel || { echo "Failed to upgrade pip or setuptools"; exit 1; }
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies from requirements.txt...'
                sh '''
                set -e
                if [ ! -f requirements.txt ]; then
                    echo "requirements.txt not found in workspace. Exiting."
                    exit 1
                fi
                ${VENV}/bin/python -m pip install --no-cache-dir --cache-dir=${PIP_CACHE} -r requirements.txt || { echo "Failed to install dependencies"; exit 1; }
                ${VENV}/bin/python -m pip list
                '''
            }
        }

        stage('Run Migrations') {
            steps {
                echo 'Running Django migrations...'
                sh '''
                set -e
                ${VENV}/bin/python ./rduploadservice/manage.py migrate --settings=${DJANGO_SETTINGS_MODULE} || { echo "Failed to run migrations"; exit 1; }
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests with pytest...'
                sh '''
                set -e
                ${VENV}/bin/python -m pytest --junitxml=test-results.xml || { echo "Tests failed"; exit 1; }
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
                ${VENV}/bin/python ./rduploadservice/manage.py collectstatic --noinput --settings=${DJANGO_SETTINGS_MODULE} || { echo "Failed to collect static files"; exit 1; }
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
