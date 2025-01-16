pipeline {
    agent any

    environment {
        VENV = "${WORKSPACE}/venv"  // Virtual environment path
        PIP_CACHE = "${WORKSPACE}/.pip-cache"  // Cache for pip installations
        DJANGO_SETTINGS_MODULE = "rduploadservice.settings"  // Django settings module
        PYTHON = "${VENV}/bin/python"  // Python executable in the virtual environment
        PYTHONPATH = "${WORKSPACE}/rduploadservice"  // Add project directory to PYTHONPATH
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
                sh """
                python3 -m venv ${VENV}  // Create a virtual environment
                source ${VENV}/bin/activate
                ${PYTHON} -m pip install --upgrade pip setuptools wheel  // Upgrade essential tools
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies from requirements.txt...'
                sh """
                source ${VENV}/bin/activate
                ${PYTHON} -m pip install --no-cache-dir -r rduploadservice/requirements.txt  // Use the correct requirements.txt path
                ${PYTHON} -m pip list  // Debugging: List installed packages
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
                    junit 'test-results.xml'  // Publish test results
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
                echo 'Debugging environment...'
                sh """
                source ${VENV}/bin/activate
                echo "Using Python binary: $(which python)"
                echo "Using Pip binary: $(which pip)"
                ${PYTHON} --version
                ${PYTHON} -m pip list
                """
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs for details.'
        }
        always {
            cleanWs()  // Clean up workspace after every build
        }
    }
}
