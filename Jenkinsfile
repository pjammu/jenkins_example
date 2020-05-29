pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Running build automation'
                sh 'cd /home/cloud_user/pycli'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt'
                archiveArtifacts artifacts: 'pycli.zip'
            }
        }
    }
 }
