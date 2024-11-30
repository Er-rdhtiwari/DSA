Here’s a list of commonly used **HTTP status codes** for different HTTP methods (**GET**, **POST**, **PUT**, **DELETE**) in various scenarios:

---

### **1. GET Method**
Used to **retrieve data** from the server.  

| **Status Code** | **Meaning**                                 | **When to Use**                                               |
|------------------|---------------------------------------------|--------------------------------------------------------------|
| `200 OK`         | Request was successful.                    | The data is successfully retrieved.                         |
| `204 No Content` | Request was successful but no data to return. | When there's no content to return for a valid GET request.   |
| `404 Not Found`  | Resource not found.                        | The requested resource does not exist on the server.         |
| `400 Bad Request`| Invalid request from the client.           | When the query parameters or input are invalid.              |
| `401 Unauthorized` | User is not authenticated.              | Authentication is required to access the resource.           |
| `403 Forbidden`  | User is authenticated but not authorized.  | When access to the resource is denied due to permissions.    |

---

### **2. POST Method**
Used to **create new resources** on the server.  

| **Status Code** | **Meaning**                                 | **When to Use**                                               |
|------------------|---------------------------------------------|--------------------------------------------------------------|
| `201 Created`    | Resource successfully created.             | A new resource was created as a result of the POST request.  |
| `202 Accepted`   | Request accepted but not yet processed.    | When the server has accepted the request but not processed it yet. |
| `400 Bad Request`| Invalid request from the client.           | Missing required fields or invalid input in the request body.|
| `409 Conflict`   | Conflict with the current state of the resource. | E.g., trying to create a resource that already exists.       |
| `500 Internal Server Error` | Server error.                  | Something went wrong on the server while handling the POST request.|

---

### **3. PUT Method**
Used to **update or replace** an existing resource.  

| **Status Code** | **Meaning**                                 | **When to Use**                                               |
|------------------|---------------------------------------------|--------------------------------------------------------------|
| `200 OK`         | Request was successful, resource updated.  | The update operation succeeded, and the updated resource is returned. |
| `204 No Content` | Request was successful but no content returned. | The update operation succeeded but doesn't return data.      |
| `400 Bad Request`| Invalid request from the client.           | Missing required fields or invalid input in the request body.|
| `404 Not Found`  | Resource not found.                        | The resource to be updated does not exist on the server.      |
| `409 Conflict`   | Conflict with the current state of the resource. | The update cannot be applied due to conflicts.               |
| `500 Internal Server Error` | Server error.                  | Something went wrong on the server while handling the PUT request.|

---

### **4. DELETE Method**
Used to **delete resources** from the server.  

| **Status Code** | **Meaning**                                 | **When to Use**                                               |
|------------------|---------------------------------------------|--------------------------------------------------------------|
| `200 OK`         | Request was successful, resource deleted.  | Resource was deleted successfully, and optional metadata is returned. |
| `204 No Content` | Request was successful, no content returned. | Resource was deleted successfully, and no additional data is returned. |
| `404 Not Found`  | Resource not found.                        | The resource to be deleted does not exist on the server.      |
| `400 Bad Request`| Invalid request from the client.           | When the request is malformed or missing required information.|
| `401 Unauthorized` | User is not authenticated.              | Authentication is required to delete the resource.           |
| `403 Forbidden`  | User is authenticated but not authorized.  | When access to delete the resource is denied due to permissions. |

---

### **General Status Codes Across All Methods**
| **Status Code** | **Meaning**                                 | **When to Use**                                               |
|------------------|---------------------------------------------|--------------------------------------------------------------|
| `500 Internal Server Error` | Unexpected server error.       | The server encountered an error while processing the request. |
| `503 Service Unavailable` | Service is temporarily unavailable. | The server is overloaded or down for maintenance.            |
| `422 Unprocessable Entity` | Input is syntactically correct but semantically invalid. | Used for validation errors in input data. |

---

### Example in Code (Wild Card Route)

Below is an example of a wildcard route that applies these status codes:

```python
@app.route("/<path:route>", methods=["GET", "POST", "PUT", "DELETE"])
def wildcard_route(route):
    if request.method == "GET":
        return jsonify({"message": "Route not implemented for GET"}), 404  # Not Found
    elif request.method == "POST":
        return jsonify({"message": "Route not implemented for POST"}), 404
    elif request.method == "PUT":
        return jsonify({"message": "Route not implemented for PUT"}), 404
    elif request.method == "DELETE":
        return jsonify({"message": "Route not implemented for DELETE"}), 404
    else:
        return jsonify({"message": "Invalid method"}), 405  # Method Not Allowed
```

---

### Best Practices:
1. **Use Appropriate Status Codes**:
   - Always return status codes that correctly reflect the outcome of the operation.
   - Avoid using `200 OK` for every response, even if there’s an error.

2. **Provide Clear Error Messages**:
   - Include messages in the response body to help clients understand the problem.

3. **Use `204` When No Content is Returned**:
   - For successful operations that don’t require a response body (e.g., DELETE).

4. **Avoid Ambiguous Codes**:
   - Use `422` instead of `400` when input is valid JSON but fails validation rules.

5. **Log Server Errors (`500`)**:
   - Ensure all `500` errors are logged for debugging.

Let me know if you’d like a more detailed implementation for a specific method or scenario!