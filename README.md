# Rick & Morty Data Service – DevOps Project

This project was created as part of a DevOps engineering assignment.  
It includes data collection from the Rick & Morty API, a REST service, Dockerization, Kubernetes deployment, Helm chart, and a full CI/CD pipeline using GitHub Actions.

---

# 📌 Part 1 – Data Collection (Core Requirement)

The project includes a data collection flow that fetches characters from the **Rick and Morty API** and filters them based on:

- Species = **Human**
- Status = **Alive**
- Origin = **Earth**

The filtering logic is implemented inside:

```
api_client.py   → Fetches data from the official Rick & Morty API  
filters.py      → Applies filtering rules  
server.py       → Exposes the filtered data via REST API  
```

---

# 📌 Part 2 – CSV Generation

A separate script (`main.py`) consumes the **local REST API** and generates a CSV file.

### Run CSV generator:

```bash
python main.py
```

This will create:

```
characters.csv
```

The CSV contains:

```
Name,Location,Image
Rick Sanchez,Earth,https://rickandmortyapi.com/api/character/avatar/1.jpeg
...
```

---

# 📌 Part 3 – REST API Service (Bonus)

The project exposes a REST API using **FastAPI**.

### Endpoints

| Endpoint | Description |
|---------|-------------|
| `/characters` | Returns filtered characters as JSON |
| `/healthcheck` | Returns service health status |

---

# 📌 Part 4 – Docker (Bonus)

The application is fully Dockerized.

### Build the Docker image

```bash
docker build -t rickmorty-api:latest .
```

### Run the container

```bash
docker run -p 8000:8000 rickmorty-api:latest
```

### Local API URLs (Docker)

```
http://localhost:8000/characters
http://localhost:8000/healthcheck
```

---

# 📌 Part 5 – Kubernetes Manifests (Bonus)

Inside the `yamls/` folder you will find:

- `Deployment.yaml`
- `Service.yaml`
- `Ingress.yaml`

### Deploy to Kubernetes

```bash
kubectl apply -f yamls/Deployment.yaml
kubectl apply -f yamls/Service.yaml
kubectl apply -f yamls/Ingress.yaml
```

### Kubernetes DNS (via Ingress)

The Ingress exposes the service at:

```
http://rick.local/characters
http://rick.local/healthcheck
```

(Defined in `Ingress.yaml` under `host: rick.local`)

---

# 📌 Part 6 – Helm Chart (Bonus)

A full Helm chart is available under `helm/`.

### Deploy using Helm

```bash
helm upgrade --install rickmorty ./helm -f ./helm/values.yaml
```

---

# 📌 Part 7 – CI/CD Pipeline (Bonus)

A GitHub Actions workflow performs:

1. Creates a **kind** Kubernetes cluster  
2. Builds the Docker image  
3. Loads the image into the cluster  
4. Deploys the application using Helm  
5. Waits for pods to become ready  
6. Runs automated tests against the `/characters` endpoint  

The workflow file is located at:

```
.github/workflows/ci-cd.yml
```

### Pipeline Steps

- **Checkout** repository  
- **Create** Kubernetes cluster  
- **Build** Docker image  
- **Load** image into cluster  
- **Deploy** using Helm  
- **Validate** deployment with curl  

A successful run confirms the entire system works end‑to‑end.

---

# 📌 Access for Reviewer

Read access was granted to:

```
chene@elementor.com
```

---

# 📌 Project Structure

```
.
├── server.py
├── api_client.py
├── filters.py
├── writer.py
├── main.py
├── characters.csv
├── Dockerfile
├── yamls/
│   ├── Deployment.yaml
│   ├── Service.yaml
│   └── Ingress.yaml
├── helm/
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
└── README.md
```

---

# 📌 Summary

This project demonstrates:

- API data collection  
- CSV generation  
- REST API development  
- Docker packaging  
- Kubernetes deployment  
- Helm chart management  
- Full CI/CD automation  

It covers **all required tasks** and **all bonus sections** of the assignment.
