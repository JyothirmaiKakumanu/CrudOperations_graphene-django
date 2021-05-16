#Clone Repository $ git clone https://github.com/JyothirmaiKakumanu/CrudOperations_graphene-django.git $ docker-compose up

Now you can access the application at http://localhost:8000/graphql and the admin site at https://localhost/admin.

#Deployment

Build app image docker build -t kubernetes-django . Create deployment kubectl apply -f deployment.yml Expose service kubectl expose deploy kubernetes-django-deployment --type=NodePort Get mapped port for the app kubectl get service Visit http://localhost: in the browser. App should be updated to the new version now.

Django polls app is started now, but a database is still empty. The next step is to complete DB migration:

docker exec -it djangopollskubernetes_django_1 python manage.py migrate DB is initialized. Let's create django user:

docker exec -it djangopollskubernetes_django_1 python manage.py createsuperuser

Google container engine We will deploy polls to GKE. It offers two services we need:

kubernetes container registry Create a basic cluster in google cloud engine. More info you can find in GKE documentation. Also write zone, cluster and project ID to some place.

Creating a GKE cluster Now that the Docker image is stored in Container Registry, create a GKE cluster to run hello-app. A GKE cluster consists of a pool of Compute Engine VM instances running Kubernetes, the open source cluster orchestration system that powers GKE.

Visit the Google Kubernetes Engine menu in Cloud Console.

Visit the Google Kubernetes Engine menu

Click add_box Create.

Choose Standard or Autopilot mode and click Configure.

In the Name field, enter the name hello-cluster.

Select a zone or region:

Standard cluster: Under Location type, select Zonal and then select a Compute Engine zone from the Zone drop-down list, such as us-west1-a.

Autopilot cluster: Select a Compute Engine region from the Region drop-down list, such as us-west1.

Click Create. This creates a GKE cluster.

Wait for the cluster to be created. When the cluster is ready, a green check mark appears next to the cluster name.

Deploying the sample app to GKE Visit the GKE Workloads menu in Cloud Console.

Visit the Workloads menu

Click add_box Deploy.

In the Container section, select Existing container image.

In the Image path field, click Select.

In the Select container image pane, select the hello-app image you pushed to Container Registry and click Select.

In the Container section, click Done, then click Continue.

In the Configuration section, under Labels, enter app for Key and hello-app for Value.

Under Configuration YAML, click View YAML. This opens a YAML configuration file representing the two Kubernetes API resources about to be deployed into your cluster: one Deployment, and one HorizontalPodAutoscaler for that Deployment.

Click Close, then click Deploy.

When the Deployment Pods are ready, the Deployment details page opens.

Under Managed pods, note the three running Pods for the hello-app Deployment.
