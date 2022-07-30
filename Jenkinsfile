pipeline {
    options {
        buildDiscarder(logRotator(numToKeepStr: ‘20', daysToKeepStr: ‘5'))
    }
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
                }
                git 'https://github.com/zinaM59/first_project.git'
            }
        }
        stage('run python') {
            steps {
                script {

                        bat 'start /min python rest_app.py'

                }
                script {

                       bat 'start /min python web_app.py'

                }
                script {

                       bat 'python backend_testing.py'

                }
                script {

                       bat 'python frontend_testing.py'

                }
                script {

                      bat 'python combined_testing.py'

                }
                script {

                      bat 'python clean_environment.py'

                }


            }
        }
    }
}
