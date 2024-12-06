To connect **RedisInsight** to a Redis instance running inside a Docker container on your Windows system, follow these steps:

---

### 1. **Ensure Redis Container is Running**
Run the following command to check if your Redis container is active:

```bash
docker ps
```

Look for the Redis container in the list and note the **container name** or **ID** and the exposed port (default is `6379`).

---

### 2. **Expose Redis Port**
If you haven't already exposed the Redis port while starting the container, stop the container and restart it with the port mapping:

```bash
docker run --name redis -d -p 6379:6379 redis
```

This maps the Redis container's `6379` port to your host's `6379` port.

---

### 3. **Download and Install RedisInsight**
1. Go to the [RedisInsight Download Page](https://redis.com/redis-enterprise/redis-insight/).
2. Download the version compatible with Windows.
3. Install and launch the application.

---

### 4. **Connect RedisInsight to Redis**
1. Open **RedisInsight**.
2. Click on **Add Redis Database**.
3. Enter the following details:
   - **Host:** `localhost`  
     (or use `127.0.0.1` as the host if `localhost` doesn't work).
   - **Port:** `6379`  
     (or the port you've mapped when running the container).
   - **Name:** Give the connection a descriptive name, e.g., `My Redis Docker`.
4. Click **Add Database**.

---

### 5. **Test the Connection**
RedisInsight should now connect to the Redis instance running in your Docker container. You'll see a dashboard where you can:
- Browse keys.
- View data structures.
- Run Redis commands using the built-in CLI.

---

### Troubleshooting Connection Issues
If you face issues:
1. **Verify Docker Networking**  
   Ensure the Redis container's `6379` port is correctly mapped to the host machine.
   ```bash
   docker port redis
   ```

2. **Check Firewall Settings**  
   Ensure no firewall or security software blocks the connection to `localhost:6379`.

3. **Container Logs**  
   Check Redis container logs to ensure the Redis server is running without errors:
   ```bash
   docker logs redis
   ```

---

Let me know if you encounter any issues during setup!