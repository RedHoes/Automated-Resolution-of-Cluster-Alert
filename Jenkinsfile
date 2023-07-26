@Library('nfq-library') _

pipeline {
  agent any

  options {
    ansiColor('xterm')
    timestamps()
    disableConcurrentBuilds()
  }

  stages {
    stage('Build') {
      steps {
        script {
          d13Build()
        }
      }
    }
    stage('Deployment') {
      steps {
        script {
          d13Deployment()
        }
      }
    }
  }
  post {
    always {
      d13Clean()
      cleanWs()
    }
  }
}
