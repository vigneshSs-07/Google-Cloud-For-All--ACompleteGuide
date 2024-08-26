### https://codelabs.developers.google.com/codelabs/cloud-app-engine-python3#0

gcloud app deploy

gcloud app browse

First, retrieve your web app hostname with the gcloud app describe command:


APPENGINE_HOSTNAME=$(gcloud app describe --format "value(defaultHostname)")


curl https://$APPENGINE_HOSTNAME



### Setup python environment:
sudo apt install python3 -y
sudo apt install python3.11-venv
python3 -m venv create myvenv
source myvenv/bin/activate

### From within your helloworld directory where the app's app.yaml configuration file is located, start the Google Cloud development server with the following command:

dev_appserver.py app.yaml