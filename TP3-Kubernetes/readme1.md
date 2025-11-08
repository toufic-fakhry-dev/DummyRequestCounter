# Kubernetes 101 – Flask Requests Counter + Redis on Docker Desktop

This lab demonstrates how to **deploy a simple Flask web application with Redis** on **Kubernetes (Docker Desktop)**.  
It covers the essential Kubernetes concepts: Deployments, Services, Scaling, Sidecar Logging, Monitoring, and Self-Healing.  
The setup was tested locally using **Docker Desktop with Kubernetes enabled**.

## Repo Structure
```
TP3-Kubernetes/
│
├── app/
│   ├── app.py              
│   └── Dockerfile          
│
├── k8s/
│   ├── counter-deployment.yaml                
│   ├── counter-deployment-with-sidecar.yaml   
│   ├── counter-service.yaml                   
│   ├── redis-deployment.yaml                  
│   └── redis-service.yaml                     
│              
└── readme1.md             
```

## Step 1 – Enable Kubernetes in Docker Desktop

1. Open **Docker Desktop → Settings → Kubernetes**  
2. Check **Enable Kubernetes**, then click **Apply & restart**
3. Verify the cluster is ready:
   ```bash
   kubectl get nodes
Output:
NAME             STATUS   ROLES                  AGE   VERSION
docker-desktop   Ready    control-plane,master   5m    v1.xx.x

4. Build the pyhton app
    ```bash
    cd app
    docker build -t requests-counter:1.0 .
    
## Step 2 – Build the Flask Application Image
1. Navigate to the 'app/' folder
2. Build the Docker image:
     ```bash
     docker build -t requests-counter:1.0 .
4. Verify the image:
   docker images

We create a local Docker image for the Flask app. Since Docker Desktop’s Kubernetes shares the same Docker engine, it can use this local image directly without pushing to Docker Hub.

## Step 3 – Deploy Redis and the Flask App
1. Apply the Redis deployment and service:
   ```bash
   kubectl apply -f k8s/redis-deployment.yaml
   kubectl apply -f k8s/redis-service.yaml

3. Apply the Flask app deployment and service:
   ```bash
   kubectl apply -f k8s/counter-deployment.yaml
   kubectl apply -f k8s/counter-service.yaml

5. Verify resources:
   ```bash
   kubectl get deploy,po,svc

Redis acts as the backend database storing the request count.
The Flask app connects to Redis using environment variables (REDIS_HOST, REDIS_PORT) defined in the YAML manifests.
Both components are managed by Kubernetes Deployments for reliability.

## Step 4 – Access the Application
1. Identify the NodePort service:
   ```bash
   kubectl get svc counter-service

3. Open the app in a browser:
   http://localhost:30080/
Output:
{"message": "Hello from Flask + Redis!", "visits": 1}

The app is exposed through a NodePort (30080), mapping external traffic from your machine to internal port 5000 inside the pod.
Each refresh increments the counter stored in Redis.

## Step 5 – Scale the Application
1. Increase the number of replicas:
   ```bash
   kubectl scale deployment counter-deployment --replicas=3

3. Verify:
   ```bash
   kubectl get pods -o wide
   
Kubernetes automatically creates 3 pods of the Flask app and balances incoming requests across them using the Service.
All pods use the same Redis backend, ensuring a consistent visits count across replicas.

## Step 6 – Add Logging with a Sidecar Container
1. Apply the updated deployment with the sidecar:
   ```bash
   kubectl apply -f k8s/counter-deployment-with-sidecar.yaml

3. Wait for rollout:
   ```bash
   kubectl rollout status deploy/counter-deployment

5. View logs from the sidecar:
   ```bash
   kubectl logs deploy/counter-deployment -c log-shipper
Output:
Visit number: 1
Visit number: 2
Visit number: 3

The sidecar container (log-shipper) tails the shared volume /var/log/app/app.log that the Flask container writes to.
This demonstrates the sidecar pattern, where secondary containers provide auxiliary services like logging or monitoring.

## Step 7 – Monitor and Troubleshoot
Useful commands:
    ```bash
  -     kubectl get pods
  -     kubectl describe pod <pod-name>
  -     kubectl logs <pod-name> -c counter
  -     kubectl logs <pod-name> -c log-shipper

kubectl describe provides detailed pod information including container states, events, and errors.
kubectl logs helps inspect output from either the app container or the sidecar container.

## Step 8 – Demonstrate Kubernetes Self-Healing
1. Delete one running pod manually:
   ```bash
   kubectl delete pod <pod-name>

3. Watch Kubernetes recreate a new one:
   ```bash
   kubectl get pods -w
   
Kubernetes maintains the desired state defined in the Deployment.
When a pod fails or is deleted, the controller immediately starts a replacement — showcasing Kubernetes self-healing capability.
