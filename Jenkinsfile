pipeline {
    agent any

    environment {
        // Virtual environment in the Jenkins workspace
        VENV = "/Users/gabrielodame/.jenkins/venv"
        PIP_CACHE = "/Users/gabrielodame/.jenkins/.pip-cache"
        DJANGO_SETTINGS_MODULE = "rduploadservice.settings" // Django settings module
        PYTHON = "${VENV}/bin/python" // Python executable in the virtual environment
        PYTHONPATH = "/Users/gabrielodame/.jenkins/workspace/rduploadservice" // Add project directory to PYTHONPATH
    }

    stages {
        stage('Initialize') {
            steps {
                echo 'Cleaning workspace and preparing environment...'
                cleanWs() // Ensure workspace is clean
            }
        }

        stage('Checkout Code') {
            steps {
                echo 'Checking out source code...'
                checkout scm // Pull the latest code from source control
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                sh """
                python3 -m venv ${VENV} // Create virtual environment
                source ${VENV}/bin/activate
                ${PYTHON} -m pip install --upgrade pip setuptools wheel // Upgrade essential tools
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies from requirements.txt...'
                sh """
                source ${VENV}/bin/activate
                ${PYTHON} -m pip install --no-cache-dir --cache-dir=${PIP_CACHE} -r rduploadservice/requirements.txt
                ${PYTHON} -m pip list // Debugging: List installed packages
                """
            }
        }

        stage('Run Migrations') {
            steps {
                echo 'Running Django migrations...'
                sh """
                source ${VENV}/bin/activate
                ${PYTHON} ./rduploadservice/manage.py migrate --settings=${DJANGO_SETTINGS_MODULE}
                """
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests with pytest...'
                sh """
                source ${VENV}/bin/activate
                ${PYTHON} -m pytest --junitxml=test-results.xml
                """
            }
            post {
                always {
                    junit 'test-results.xml' // Publish test results
                }
            }
        }

        stage('Static Files Collection') {
            steps {
                echo 'Collecting static files for deployment...'
                sh """
                source ${VENV}/bin/activate
                ${PYTHON} ./rduploadservice/manage.py collectstatic --noinput --settings=${DJANGO_SETTINGS_MODULE}
                """
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh """
                echo "Deploy step is a placeholder. Add deployment commands here."
                """
            }
        }

        stage('Debug Environment') {
            steps {
                echo 'Debugging environment and permissions...'
                sh """
                echo "Current user: $(whoami)"
                echo "Current directory: $(pwd)"
                ls -ld /Users/gabrielodame/.jenkins
                ls -ld /Users/gabrielodame/.jenkins/workspace
                """
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
            sh "rm -rf ${VENV}" // Remove the virtual environment after execution
            cleanWs() // Clean up the workspace
        }
    }
}
