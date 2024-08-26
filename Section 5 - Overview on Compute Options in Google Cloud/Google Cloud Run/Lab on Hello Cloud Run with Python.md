
### https://codelabs.developers.google.com/codelabs/cloud-run-hello-python3#4
https://cloud.google.com/blog/products/serverless/build-and-deploy-an-app-to-cloud-run-with-a-single-command
https://codelabs.developers.google.com/codelabs/cloud-run-dev2prod#0

gcloud services enable \
  artifactregistry.googleapis.com \
  cloudbuild.googleapis.com \
  run.googleapis.com

To test the application, create a virtual environment:


virtualenv venv
Activate the virtual environment:


source venv/bin/activate
Install the dependencies:


pip install -r requirements.txt
You should get a confirmation message like the following:


...
Successfully installed Flask ... gunicorn ...
Start the application:


python main.py
The logs show that you are in development mode:


 * Serving Flask app 'main'
 * Debug mode: on
   WARNING: This is a development server.
   Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Running on http://localhost:8080
   Press CTRL+C to quit
...



REGION="europe-west9"

Deploy the application to Cloud Run:


gcloud run deploy helloworld-python \
  --source . \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated


SERVICE_URL=$( \
  gcloud run services describe helloworld-python \
  --platform managed \
  --region $REGION \
  --format "value(status.url)" \
)
echo $SERVICE_URL


curl $SERVICE_URL?who=me