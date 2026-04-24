# 🚀 Retail API DevOps Project

A production-style cloud-native retail application built to demonstrate real-world DevOps practices using Flask, Docker, Kubernetes, Ingress, and CI/CD automation.

---

# 📌 Project Overview

This project simulates how modern applications are developed, containerized, deployed, exposed, and managed in Kubernetes environments.

The goal is to build a **portfolio-grade DevOps project** that showcases end-to-end skills:

```text
Code → Containerize → Push Registry → Deploy Kubernetes → Expose via Ingress → Automate CI/CD → Monitor → Cloud Deploy
```

---

# 🧰 Tech Stack

* Python + Flask – Backend API
* Docker – Container packaging
* Kubernetes – Workload orchestration
* NGINX Ingress Controller – HTTP routing
* Docker Hub – Image registry
* GitHub – Source control
* GitHub Actions – CI/CD (planned)
* Prometheus – Metrics (app-ready)
* Grafana – Dashboards (planned)
* Amazon Web Services – Future cloud hosting (planned)

---

# 🏗️ Architecture

![Image](https://images.openai.com/static-rsc-4/-P9ZpphRTuvkb2gHCh7jjrojjIQ5jNoqwz1CjTxtEMaBpGUbyyqe7bNhizfG8JOnr7s4c_8U3XgiztZleErEIQnjoKb8uZsahXfKGr9A2cvgN1J0v43s9DXYLJbWcKdRJu1i9DzZoZpMJXMNugulIe0c4gwOLjIXiJJSbmLQ93PvVqsc2P8328antEGnl6Q5?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/tVPuTMPGOu4keFa-xX0IS77XhG1AG9CIi0ueq0551jiDZowDnPfbdw7BXRep91aasZzvFRIP6JwQPmlmCIVMf_tskj7sTootfheptc0J9qFtLdjV825SArCdiW7zVIn3afD-Z8yaofB4bW1SghJiveK81J06MFMJGa0JUKcplbocGBV_D4dnIlPhd8xDMSkp?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/UWOWr6EqiDsLAAmznSNs5cMyFx9NRlLyMiwsEPbV055CLX70H9UH33krxSjorvmeh09HaMJWJXbKsHfbVc0fDYgff3Fwo3YpZkD7R2Y02zuHJHBBT2a9GYSsrcgo9GQGTTWP6GMFb7cGIiIeX0WEKq8yRTZXbc7wSBXozifJ68B6RYvml4ITJg4r0xHUXh6X?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/-d7FVOmKFT4lKEYbY6a5VAZr69PkQpWzu4l_lOrXXlgQbZGtvI5YzCeoffPK91dywvnKNetYk6bj7ZV5sy7XlBxfzXm_vVscpIaYyywJ9tuadordRA1wQNa9ZSvUIqCa9L3L633-24k_bhEudcpjjCQDRagSUCF1XA9mR9nush8i-PgMn2Fyl8AcmbGwyctp?purpose=fullsize)

```text
Browser
  ↓
Ingress (retail-app.local)
  ↓
Kubernetes Service
  ↓
Retail API Pods (ReplicaSet)
  ↓
Docker Container running Flask App
```

---

# 📁 Project Structure

```
retail-devops-project/
├── app.py
├── requirements.txt
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── ingress.yaml
├── .github/workflows/         # CI/CD (to be added)
└── README.md
```

---

# ✅ Implemented Features

## 1️⃣ Flask Retail API

Created a Python Flask backend with endpoints:

| Endpoint    | Purpose             |
| ----------- | ------------------- |
| `/`         | Landing page        |
| `/products` | Sample product data |
| `/health`   | Health status       |
| `/ready`    | Readiness check     |
| `/metrics`  | Prometheus metrics  |

### Why implemented?

To simulate a real backend service with production health checks and observability.

---

## 2️⃣ Dockerized Application

Created a Docker image for the Flask application.

### Why implemented?

* Consistent runtime across environments
* Easy deployment
* Required for Kubernetes

---

## 3️⃣ Docker Hub Registry Push

Application image pushed to Docker Hub.

### Why implemented?

Kubernetes clusters need a registry to pull images from.

---

## 4️⃣ Kubernetes Deployment

Created Deployment manifest with:

* Multiple replicas
* Rolling updates
* Resource requests/limits
* Liveness probes
* Readiness probes

### Why implemented?

To run containers reliably and manage scaling/self-healing.

---

## 5️⃣ Kubernetes Service

Created Service resource for stable networking and pod load balancing.

### Why implemented?

Pods are ephemeral. Services provide a stable access point.

---

## 6️⃣ Ingress Routing

Configured Ingress and accessed app using:

```text
http://retail-app.local/health
```

### Why implemented?

Ingress simulates real production traffic routing and custom domain access.

---

## 7️⃣ Basic Namespace Isolation

Used separate namespace:

```text
retail
```

### Why implemented?

Logical separation of resources inside Kubernetes.

---

# 🔍 Current Skills Demonstrated

* Linux / CLI workflow
* Git usage
* Python API deployment
* Docker build/tag/push
* Kubernetes core objects
* Networking (Service / Ingress)
* Troubleshooting image pull errors
* Health probes
* Rolling updates

---

# 🚧 To Be Implemented (Next Phases)

## 1️⃣ CI Pipeline with GitHub Actions

### Plan:

On every push:

```text
Build image → Push Docker Hub
```

### Why?

Removes manual builds and introduces automation.

---

## 2️⃣ Continuous Deployment (CD)

### Plan:

Auto update Kubernetes deployments after successful CI.

### Why?

Real DevOps workflow with faster releases.

---

## 3️⃣ Monitoring Stack

### Plan:

Install Prometheus + Grafana.

### Why?

Track:

* CPU / memory
* Pod restarts
* Request rates
* Application metrics

---

## 4️⃣ Logging Stack

### Plan:

Centralized logs using EFK / ELK.

### Why?

Essential for debugging distributed systems.

---

## 5️⃣ Secrets & ConfigMaps

### Plan:

Move configuration from code into Kubernetes resources.

### Why?

Secure and clean configuration management.

---

## 6️⃣ Terraform Infrastructure

### Plan:

Provision AWS infrastructure using Terraform.

### Why?

Infrastructure as Code is a core DevOps skill.

---

## 7️⃣ AWS Deployment

### Plan:

Deploy to EKS / EC2.

### Why?

Shows real cloud deployment capability.

---

## 8️⃣ GitOps with Argo CD

### Plan:

Use Git as source of truth for deployments.

### Why?

Modern Kubernetes delivery model.

---

# 🧪 How to Run Locally

## Run Flask App

```bash
pip install -r requirements.txt
python app.py
```

## Build Docker Image

```bash
docker build -t retail-api:v1 .
```

## Run Container

```bash
docker run -p 5000:5000 retail-api:v1
```

---

# ☸️ Kubernetes Deploy

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml
```

---

# 🌐 Access Application

```text
http://retail-app.local/
http://retail-app.local/health
http://retail-app.local/products
```

---

# 📈 Why This Project Matters

This project demonstrates practical DevOps knowledge beyond theory:

* Build once, run anywhere
* Container orchestration
* Service exposure
* Infrastructure automation readiness
* CI/CD readiness
* Cloud migration readiness

---

# 🎯 Future Goal

Convert this into a fully production-grade platform with:

```text
GitHub Actions + ArgoCD + Terraform + AWS + Monitoring
```

---

# 👨‍💻 Author

Kavin Prasad S
DevOps Engineer | Kubernetes | Docker | Linux | Cloud Learning Journey

---
