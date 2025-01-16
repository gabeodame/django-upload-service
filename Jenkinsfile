pipeline {
    agent any

    environment {
        VENV = "/Users/gabrielodame/.jenkins/python-venv" // Virtual environment path outside workspace
        PIP_CACHE = "/Users/gabrielodame/.jenkins/.pip-cache" // pip cache directory
        DJANGO_SETTINGS_MODULE = "rduploadservice.settings" // Django settings module
        PYTHON = "/Users/gabrielodame/.jenkins/python-venv/bin/python" // Python binary inside virtual environment
        PYTHONPATH = "${WORKSPACE}/rduploadservice" // Add project directory to PYTHONPATH
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
                set -e  # Exit immediately if any command fails

                # Create virtual environment if it doesn't already exist
                if [ ! -d "/Users/gabrielodame/.jenkins/python-venv" ]; then
                    echo "Creating virtual environment..."
                    python3 -m venv /Users/gabrielodame/.jenkins/python-venv
                else
                    echo "Virtual environment already exists."
                fi

                # Upgrade pip and essential tools
                /Users/gabrielodame/.jenkins/python-venv/bin/python -m pip install --upgrade pip setuptools wheel
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies from requirements.txt...'
                sh '''
                set -e

                # Ensure virtual environment is active
                if [ ! -f "/Users/gabrielodame/.jenkins/python-venv/bin/activate" ]; then
                    echo "Error: Virtual environment not found. Please check the setup stage."
                    exit 1
                fi

                # Install dependencies
                /Users/gabrielodame/.jenkins/python-venv/bin/python -m pip install --no-cache-dir --cache-dir=/Users/gabrielodame/.jenkins/.pip-cache -r rduploadservice/requirements.txt
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
                    junit 'test-results.xml' // Publish test results
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

        stage('Debug Environment') {
            steps {
                echo 'Debugging environment and permissions...'
                sh '''
                echo "Current user: $(whoami)"
                echo "Current directory: $(pwd)"
                echo "Python version:"
                /Users/gabrielodame/.jenkins/python-venv/bin/python --version
                echo "Virtual environment contents:"
                ls -l /Users/gabrielodame/.jenkins/python-venv/bin
                echo "Workspace contents:"
                ls -l ${WORKSPACE}
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
