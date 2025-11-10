🚀 Kubernetes 101 — Requests Counter App

🧭 Overview
This project was completed as part of the Kubernetes 101 Workshop.
It demonstrates a full DevOps workflow: containerization, deployment on Kubernetes, scaling, logging, monitoring, and self-healing — all using Docker Desktop as a local cluster.

🧩 Project Structure
app/
 ├─ main.py              # Flask + Redis counter app
 ├─ requirements.txt     # Python dependencies
 └─ Dockerfile           # Builds counter-app:local image

k8s/
 ├─ redis.yaml           # Redis Deployment + ClusterIP Service
 ├─ counter-deployment.yaml  # Counter app Deployment + logging sidecar
 └─ counter-service.yaml     # NodePort Service (port 32080)

🧱 Technologies

Python 3.12 / Flask / Redis

Docker Desktop + Kubernetes v1.34.1

kubectl CLI

BusyBox (for log sidecar)

Git + GitHub (for version control)

🧠 Workshop Parts
Part 1 – Setting Up Kubernetes

Enabled Kubernetes in Docker Desktop → verified single-node cluster using: kubectl get nodes

Part 2 – Deploying the Requests Counter App

Built the Flask app container (counter-app:local), deployed alongside Redis.
Services:

Redis → internal ClusterIP 6379

Counter App → external NodePort 32080
Accessible at http://localhost:32080

Part 3 – Scaling the Application

Scaled from 1 to 3 replicas:

kubectl scale deploy/counter --replicas=3


Kubernetes load-balances requests; Redis keeps a shared counter.

Part 4 – Logging Sidecar

Added a BusyBox sidecar to tail /var/log/app/app.log in the same Pod.
Verified dual containers (app, log-sidecar) and live logs using:

kubectl logs deploy/counter -c log-sidecar

Part 5 – Monitoring & Troubleshooting

Observed and debugged cluster behavior with:

kubectl get pods
kubectl describe pod <pod-name>
kubectl logs <pod-name>


Deleted Pods to demonstrate self-healing via automatic recreation.

🧰 Key Kubernetes Concepts Applied

Pods & multi-container patterns

Deployments & ReplicaSets

Services (ClusterIP & NodePort)

Volumes (shared logging)

Scaling and self-healing

Observability via logs

Version control with Git/GitHub

🏁 Result

✅ Fully working Kubernetes setup running a Python + Redis Requests Counter App with:

Containerization (Docker)

Orchestration (Kubernetes)

Scalability & Self-Healing

Centralized Logging (sidecar)

Git-based version control

