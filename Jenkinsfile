pipeline {
  agent any
  stages {
    stage('Build Image') {
      steps {
        sh 'docker build -t localhost:5000/${IMAGE_NAME}:${BUILD_NUMBER} .'
      }
    }
    stage('Push Image') {
      steps {
        sh 'docker push localhost:5000/${IMAGE_NAME}:${BUILD_NUMBER}'
      }
    }
    stage('Distribute') {
      steps {
        sh '''curl -s --fail --header "Content-Type: application/json" \\
  --request POST \\
  --data \'{   "url" : "\'${REGISTRY}\'",   "tag" : "\'${BUILD_NUMBER}\'",   "image" : "\'${IMAGE_NAME}\'" }\' \\
  ${AGENT1}/pull'''
      }
    }
    stage('Test') {
      steps {
        sh '''curl -s --header "Content-Type: application/json" \\
  --request POST \\
  --data \'{   "url" : "\'${REGISTRY}\'",   "tag" : "\'${BUILD_NUMBER}\'",   "image" : "\'${IMAGE_NAME}\'" }\' \\
  ${AGENT1}/test -o test.log'''
        archiveArtifacts 'test.log'
      }
    }
    stage('Check logs') {
      steps {
        sh '''#!/bin/bash
grep -B4 "FAILED" test.log

ret=$?
if [ $ret -eq 0 ]; then
exit 1
else
    exit 0
fi'''
      }
    }
  }
  environment {
    IMAGE_NAME = 'eero'
    REGISTRY = '192.168.78.110:5000'
    AGENT1 = '192.168.79.83:8000'
  }
}