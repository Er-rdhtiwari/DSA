### Manual Testing with cURL and Postman

#### Login
```bash
curl -X POST http://127.0.0.1:5000/login \
-H "Content-Type: application/json" \
-d '{"username": "admin_user", "password": "admin123"}'
```

#### View Resources
```bash
curl -X GET http://127.0.0.1:5000/resources \
-H "Authorization: Bearer <TOKEN>"
```

#### Edit Resource (Only Developer or Admin)
```bash
curl -X PUT http://127.0.0.1:5000/resources/1 \
-H "Authorization: Bearer <TOKEN>" \
-H "Content-Type: application/json" \
-d '{"name": "Updated Resource", "description": "Updated Description"}'
```

#### Delete Resource (Only Admin)
```bash
curl -X DELETE http://127.0.0.1:5000/resources/1 \
-H "Authorization: Bearer <TOKEN>"
```

#### Add Resource (Developer or Admin)
```bash
curl -X POST http://127.0.0.1:5000/resources \
-H "Authorization: Bearer <TOKEN>" \
-H "Content-Type: application/json" \
-d '{"name": "New Resource", "description": "Description of the new resource"}'
```

---

### How to Test in Postman
1. **Login Endpoint:**
   - Method: `POST`
   - URL: `http://127.0.0.1:5000/login`
   - Body (JSON):
     ```json
     {
       "username": "admin_user",
       "password": "admin123"
     }
     ```

2. **Other Endpoints:**
   - Copy the JWT token from the `login` response.
   - Add it to the Authorization header:
     - Key: `Authorization`
     - Value: `Bearer <TOKEN>` (replace `<TOKEN>` with the actual token).
   - Test the other endpoints using their respective methods and body (if required).