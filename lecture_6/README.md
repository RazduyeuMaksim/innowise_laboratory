# lecture_6

## 🚀 Docker

### Description
A simple FastAPI application packaged and run inside a Docker container.

The goal of this task is to demonstrate how to dockerize a Python web application and manage it using basic Docker commands.

The application exposes a single endpoint used to verify that the container is running correctly.

---

###  Application behavior
The API provides the following endpoint:

- `GET /healthcheck`  
  Returns a JSON response:
  ```json
  { "status": "ok" }