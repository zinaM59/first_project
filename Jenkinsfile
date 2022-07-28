pipeline {
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


            }
        }
    }
}
//         stage('run python') {
//             steps {
//                 script {
//                     if (checkOs() == 'Windows') {
//                         bat 'start /min python web_app.py'
//                     } else {
//                         sh 'nohup python web_app.py&'
//                     }
//                 }
//             }
//         }
//         stage('run python') {
//             steps {
//                 script {
//                     if (checkOs() == 'Windows') {
//                         bat 'python backend_testing.py'
//                     } else {
//                         sh 'python backend_testing.py'
//                     }
//                 }
//             }
//         }
//         stage('run python') {
//             steps {
//                 script {
//                     if (checkOs() == 'Windows') {
//                         bat 'python frontend_testing.py'
//                     } else {
//                         sh 'python frontend_testing.py'
//                     }
//                 }
//             }
//         }
//         stage('run python') {
//             steps {
//                 script {
//                     if (checkOs() == 'Windows') {
//                         bat 'python combined_testing.py'
//                     } else {
//                         sh 'python combined_testing.py'
//                     }
//                 }
//             }
//         }
//         stage('run python') {
//             steps {
//                 script {
//                     if (checkOs() == 'Windows') {
//                         bat 'python clean_environment.py'
//                     } else {
//                         sh 'python clean_environment.py'
//                     }
//                 }
//             }
//         }
//
//     }
// }
def checkOs(){
    if (isUnix()) {
        def uname = sh script: 'uname', returnStdout: true
        if (uname.startsWith("Darwin")) {
            return "Macos"
        }
        else {
            return "Linux"
        }
    }
    else {
        return "Windows"
    }
}