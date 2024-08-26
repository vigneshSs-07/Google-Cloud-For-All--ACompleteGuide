


Deploy a sample app to your cluster

Deploy a sample "hello world" web app provided by Google and stored as a container in Artifact Registry.

In the Google Cloud console, go to the GKE Workloads page.

Go to Workloads

Click Deploy.

Leave Existing container image selected, and in Image path enter the following path:

### us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0

This simple "hello world" app is packaged into a single container, but larger apps typically consist of several related containers that can be deployed together and run as a single workload.

Click Continue to move to the Configuration section.

In Deployment name, enter the following name:

hello-world-app
In Kubernetes Cluster, select hello-world-cluster.

Click Continue.

In the Expose section, create a load balancing Kubernetes Service to direct external requests to your app:

Select Expose deployment as a new service.

Leave Port 1 set to 80.

In Target port 1, enter 8080.

Click Deploy.

GKE automatically assigns an available external IP address to the Service.

This Service is considered to be part of the hello-world-app workload.

For Autopilot clusters, you might see an error message, such as Does not have minimum availability. This occurs because Autopilot deletes and then re-creates the nodes. Wait a few minutes, then click refreshRefresh to update the page.

Wait until the deployment completes and you see the Deployment details page.