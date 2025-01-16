pipeline {
    agent any

    environment {
        // Python environment settings
        VENV = "${WORKSPACE}/venv"
        PIP_CACHE = "${WORKSPACE}/.pip-cache"
        DJANGO_SETTINGS_MODULE = "rduploadservice.settings"
        PYTHON = "${VENV}/bin/python"
        PYTHONPATH = "${WORKSPACE}/rduploadservice"
    }

    stages {
        stage('Initialize') {
            steps {
                echo 'Preparing environment...'
                cleanWs()
            }
        }

        stage('Checkout Code') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python environment...'
                sh """
                python3 -m venv ${VENV}
                source ${VENV}/bin/activate
                ${PYTHON} -m pip install --upgrade pip setuptools wheel
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh """
                ${PYTHON} -m pip install --no-cache-dir -r requirements.txt
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
                echo 'Running tests...'
                sh """
                source ${VENV}/bin/activate
                ${PYTHON} -m pytest --junitxml=test-results.xml
                """
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }

        stage('Static Files Collection') {
            steps {
                echo 'Collecting static files...'
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
                echo "Deploying the Django application..."
                """
            }
        }
    }

    post {
        success {
            echo 'Build completed successfully!'
        }
        failure {
            echo 'Build failed. Please check logs.'
        }
        always {
            cleanWs()
        }
    }
}
