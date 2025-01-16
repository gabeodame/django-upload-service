pipeline {
    agent any

    environment {
        // Python environment settings
        VENV = "${WORKSPACE}/venv"
        PIP_CACHE = "${WORKSPACE}/.pip-cache"
        DJANGO_SETTINGS_MODULE = "rduploadservice.settings"
        PYTHON = "${VENV}/bin/python"
    }

    stages {
        stage('Initialize') {
            steps {
                echo 'Preparing environment...'
                // Clean workspace before starting
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
                ${PYTHON} -m pip install --upgrade pip
                ${PYTHON} -m pip install --upgrade setuptools wheel
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh """
                ${PYTHON} -m pip install --cache-dir ${PIP_CACHE} -r ./rduploadservice/requirements.txt
                """
            }
        }

        stage('Run Migrations') {
            steps {
                echo 'Running Django migrations...'
                sh """
                ${PYTHON} manage.py migrate --settings=${DJANGO_SETTINGS_MODULE}
                """
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh """
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
                ${PYTHON} manage.py collectstatic --noinput --settings=${DJANGO_SETTINGS_MODULE}
                """
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // Deployment logic goes here (e.g., copy files, trigger deploy scripts, etc.)
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
            // Clean up virtual environment after the build
            deleteDir()
        }
    }
}
