pipeline {
    agent any

    environment {
        VENV = "/Users/gabrielodame/.jenkins/python-venv"
        PIP_CACHE = "/Users/gabrielodame/.jenkins/.pip-cache"
        DJANGO_SETTINGS_MODULE = "rduploadservice.settings"
        PYTHON = "/Users/gabrielodame/.jenkins/python-venv/bin/python"
        PYTHONPATH = "${WORKSPACE}/rduploadservice"
        PATH = "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
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

        stage('Debug Python Version') {
            steps {
                echo 'Debugging Python version...'
                sh '''
                set -e
                echo "Global Python version:"
                python3 --version
                '''
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python virtual environment with Python 3.10...'
                sh '''
                set -e
                echo "Removing old virtual environment, if any..."
                rm -rf ${VENV}
                echo "Creating new virtual environment..."
                /usr/local/bin/python3.10 -m venv ${VENV}
                echo "Upgrading pip and tools..."
                ${VENV}/bin/python -m pip install --upgrade pip setuptools wheel
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies from requirements.txt...'
                sh '''
                set -e
                if [ ! -f requirements.txt ]; then
                    echo "requirements.txt not found. Exiting."
                    exit 1
                fi
                echo "Installing dependencies..."
                ${VENV}/bin/python -m pip install --no-cache-dir --cache-dir=${PIP_CACHE} -r requirements.txt || {
                    echo "Fallback: Installing compatible Django version."
                    ${VENV}/bin/python -m pip install Django==4.2
                }
                echo "Installed packages:"
                ${VENV}/bin/python -m pip list
                '''
            }
        }

        stage('Run Migrations') {
            steps {
                echo 'Running Django migrations...'
                sh '''
                set -e
                ${VENV}/bin/python ./rduploadservice/manage.py migrate --settings=${DJANGO_SETTINGS_MODULE}
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests with pytest...'
                sh '''
                set -e
                ${VENV}/bin/python -m pytest --junitxml=test-results.xml
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
                ${VENV}/bin/python ./rduploadservice/manage.py collectstatic --noinput --settings=${DJANGO_SETTINGS_MODULE}
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
