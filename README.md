# Docker & Kubernetes Practical Guide

## 1. Docker Basics

### Build Docker Image

```bash
docker build -t node-app .
```

### Run Container

```bash
docker run -p 3000:3000 node-app
```

### Run in Detached Mode

```bash
docker run -d -p 3000:3000 node-app
```

### List Running Containers

```bash
docker ps
```

### Stop Container

```bash
docker stop <container_id>
```

### Remove Container

```bash
docker rm <container_id>
```

### List Images

```bash
docker images
```

### Remove Image

```bash
docker rmi node-app
```

---

## 2. Dockerfile Example (Node App)

```Dockerfile
FROM node:18

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000

CMD ["node", "app.js"]
```

---

## 3. Kubernetes Basics

### Check Cluster

```bash
kubectl get nodes
```

### Get Pods

```bash
kubectl get pods
```

### Apply Deployment

```bash
kubectl apply -f deployment.yaml
```

### Apply Service

```bash
kubectl apply -f service.yaml
```

### Describe Pod

```bash
kubectl describe pod <pod_name>
```

### View Logs

```bash
kubectl logs <pod_name>
```

### Delete Deployment

```bash
kubectl delete -f deployment.yaml
```

---

## 4. Deployment YAML

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: node-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: node-app
  template:
    metadata:
      labels:
        app: node-app
    spec:
      containers:
      - name: node-app
        image: node-app
        ports:
        - containerPort: 3000
```

---

## 5. Service YAML

```yaml
apiVersion: v1
kind: Service
metadata:
  name: node-service
spec:
  type: NodePort
  selector:
    app: node-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 3000
      nodePort: 30007
```

---

## 6. Scaling

```bash
kubectl scale deployment node-app --replicas=4
```

---

## 7. Rolling Updates

```bash
kubectl set image deployment/node-app node-app=node-app:v2
```

---

## 8. Debugging

### Check Events

```bash
kubectl get events
```

### Exec into Pod

```bash
kubectl exec -it <pod_name> -- /bin/sh
```

---

## 9. Useful Tips

* Always tag images properly (node-app:v1, v2)
* Use .dockerignore to reduce image size
* Keep containers lightweight
* Use logs for debugging

---

## 10. Full Workflow Summary

1. Write Dockerfile
2. Build Image
3. Run Locally
4. Create Kubernetes YAML files
5. Apply Deployment & Service
6. Access Application
7. Scale if needed

---

This README covers all essential commands and setup used in Docker and Kubernetes practical sessions.
