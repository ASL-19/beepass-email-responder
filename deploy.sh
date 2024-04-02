#!/bin/bash

# Project config
PROJECT_ROOT=`pwd`
DIST_DIR_NAME="dist"
DEPLOY_DIR_NAME="deploy"
LAMBDA_CODE_FILE=lambda.zip

# AWS Config
LAMBDA_HANDLER=responder.mail_responder
LAMBDA_FUNCTION_NAME=${AWS_LAMBDA_FUNCTION_NAME}
REGION=${AWS_LAMBDA_REGION_NAME}
AWS_ACCOUNT=${AWS_ACCOUNT}
AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
LAMBDA_DESCRIPTION="BeePass Distribution Email Responder"
##
LAMBDA_ROLE=${LAMBDA_ROLE}
LAMBDA_TIMEOUT=300
LAMBDA_MEMORY=256
## Python version
RUNTIME=python3.8
## TAGS
TAG_ACCOUNT=${TAG_ACCOUNT}
TAG_PROJECT=${TAG_PROJECT}
TAG_PURPOSE=${TAG_PURPOSE}

update_env_variables() {
  # update function
  echo "----------------------------"
  echo "Update Environment Variables"
  echo "----------------------------"
  echo "Lambda role:"
  echo ${LAMBDA_ROLE}
  AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
  AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
  aws lambda update-function-configuration \
    --region ${REGION} \
    --function-name ${LAMBDA_FUNCTION_NAME} \
    --handler ${LAMBDA_HANDLER} \
    --description "${LAMBDA_DESCRIPTION}" \
    --role arn:aws:iam::${AWS_ACCOUNT}:role/${LAMBDA_ROLE} \
    --runtime ${RUNTIME} \
    --timeout ${LAMBDA_TIMEOUT} \
    --memory-size ${LAMBDA_MEMORY} \
    --environment '{"Variables": {"DEBUG": "False"}}'
}


update_lambda() {
  # update function
  echo "-----------------------------"
  echo "Update Lambda function on AWS"
  echo "-----------------------------"
  echo ""
  AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
  AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
  aws lambda update-function-code \
    --region ${REGION} \
    --function-name ${LAMBDA_FUNCTION_NAME} \
    --zip-file fileb://${PROJECT_ROOT}/${DEPLOY_DIR_NAME}/${LAMBDA_CODE_FILE}
}


create_lambda() {
  # create new function
  echo "-----------------------------"
  echo "Create Lambda function on AWS"
  echo "-----------------------------"
  echo ""
   AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
   AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
   aws lambda create-function \
    --region ${REGION} \
    --function-name ${LAMBDA_FUNCTION_NAME} \
    --description "${LAMBDA_DESCRIPTION}" \
    --zip-file fileb://${PROJECT_ROOT}/${DEPLOY_DIR_NAME}/${LAMBDA_CODE_FILE} \
    --role arn:aws:iam::${AWS_ACCOUNT}:role/${LAMBDA_ROLE} \
    --handler ${LAMBDA_HANDLER} \
    --runtime ${RUNTIME} \
    --timeout ${LAMBDA_TIMEOUT} \
    --memory-size ${LAMBDA_MEMORY} \
    --tags Account=${TAG_ACCOUNT},Project=${TAG_PROJECT},Purpose=${TAG_PURPOSE}
}

deploy() {
  echo "-----------------------"
  echo "Deploying to AWS Lambda"
  echo "-----------------------"
  echo ""

  # if function already exists
  if aws lambda get-function --region ${REGION} --function-name ${LAMBDA_FUNCTION_NAME} > /dev/null; then
    update_lambda
    sleep 30
    update_env_variables
  else
    create_lambda
    sleep 30
    update_env_variables
  fi
}

deploy
