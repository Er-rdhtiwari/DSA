To connect **MongoDB Compass** to a MongoDB instance running inside Docker on your Windows system, follow these steps:

---

### 1. **Verify Docker Container is Running**
Ensure your MongoDB container is running. You can check this by running:

```bash
docker ps
```

Look for your MongoDB container in the list. Note the **container name** or **ID** and the exposed port (default is `27017`).

---

### 2. **Find the Host IP**
For Docker on Windows, use **`localhost`** or **`127.0.0.1`** to connect if your MongoDB container is mapped to your local network. 

If using Docker Desktop, this usually works directly.

---

### 3. **Expose MongoDB Port**
When you run MongoDB in Docker, the port must be exposed to your local system. For example, your container should be started with:

```bash
docker run --name mongodb -d -p 27017:27017 mongo
```

This maps the container's `27017` port to your host's `27017` port. If you forgot to expose the port, stop the container and restart it with the above command.

---

### 4. **Launch MongoDB Compass**
- Open **MongoDB Compass** on your Windows machine.
- Click **"Connect"**.
- In the **Connection String** field, enter:

```plaintext
mongodb://localhost:27017
```

---

### 5. **Test the Connection**
- Click **"Connect"**.
- MongoDB Compass should successfully connect to your Dockerized MongoDB instance.

---

### 6. **If the Connection Fails**
If the connection fails:
1. **Check Container Logs**  
   Use the following command to ensure MongoDB is running without errors:
   ```bash
   docker logs mongodb
   ```
   
2. **Verify Port Mapping**  
   Ensure the `27017` port is exposed correctly.

3. **Firewall Issues**  
   If you're running in a more restricted environment, ensure no firewall is blocking connections to `localhost:27017`.

---

### Optional: **Docker Compose for Convenience**
If you use **Docker Compose**, define your MongoDB service with a port mapping in a `docker-compose.yml` file:

```yaml
version: '3.8'
services:
  mongodb:
    image: mongo
    container_name: mongodb
    ports:
      - "27017:27017"
```

Start with:

```bash
docker-compose up -d
```

You can then connect to MongoDB Compass with `mongodb://localhost:27017`.

--- 

Let me know if you encounter issues!