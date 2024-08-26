# https://codelabs.developers.google.com/codelabs/cloud-starting-cloudfunctions#6

https://codelabs.developers.google.com/codelabs/cloud-starting-cloudfunctions#0

https://codelabs.developers.google.com/codelabs/cloud-functions-python-http#2

gcloud services enable \
  cloudfunctions.googleapis.com \
  cloudbuild.googleapis.com

gcloud services enable cloudfunctions.googleapis.com

FUNCTION_NAME="hello_world"

gcloud functions deploy function-1 \
  --runtime python312 \
  --trigger-http \
  --allow-unauthenticated


Flask==2.3.2
functions-framework==3.*

------
https://cloud.google.com/functions/1stgendocs/create-deploy-http-python-1st-gen

gcloud functions describe hello_http

gcloud functions describe hello_http

gcloud functions logs read hello_http

