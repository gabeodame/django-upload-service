pipeline {
    agent any

    environment {
        VENV = "/tmp/venv-${BUILD_NUMBER}"  // Temporary directory for virtual environment
        PIP_CACHE = "${WORKSPACE}/.pip-cache"
        DJANGO_SETTINGS_MODULE = "rduploadservice.settings"
        PYTHON = "${VENV}/bin/python"
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

        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                sh """
                python3 -m venv \$VENV  // Create a virtual environment in /tmp
                source \$VENV/bin/activate
                \$PYTHON -m pip install --upgrade pip setuptools wheel  // Upgrade essential tools
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies from requirements.txt...'
                sh """
                source \$VENV/bin/activate
                \$PYTHON -m pip install --no-cache-dir -r rduploadservice/requirements.txt
                \$PYTHON -m pip list
                """
            }
        }

        stage('Run Migrations') {
            steps {
                echo 'Running Django migrations...'
                sh """
                source \$VENV/bin/activate
                \$PYTHON ./rduploadservice/manage.py migrate --settings=\$DJANGO_SETTINGS_MODULE
                """
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests with pytest...'
                sh """
                source \$VENV/bin/activate
                \$PYTHON -m pytest --junitxml=test-results.xml
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
                echo 'Collecting static files for deployment...'
                sh """
                source \$VENV/bin/activate
                \$PYTHON ./rduploadservice/manage.py collectstatic --noinput --settings=\$DJANGO_SETTINGS_MODULE
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
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
        always {
            echo 'Cleaning up temporary virtual environment...'
            sh "rm -rf /tmp/venv-${BUILD_NUMBER}"  // Cleanup temporary virtual environment
            cleanWs()
        }
    }
}
