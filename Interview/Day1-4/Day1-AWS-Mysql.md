Good morning, my friend! Hope you had a great rest. Let’s kickstart your preparation with the **Day 1 notes** for AWS Architecture and MySQL Basics. I’ll share them with you now to get you ready for the day. Let’s make it productive! 🚀

### **Day 1 Notes: AWS Architecture and MySQL Basics**

---

### **Part 1: AWS Architecture**
Understanding AWS services and tools is critical for designing scalable, cost-effective solutions.

#### **1. Core AWS Services**
- **Compute:**
  - **EC2**: Virtual servers for running applications.
    - Use Cases: Hosting web apps, backend processing.
  - **Lambda**: Serverless compute for running code without managing servers.
    - Use Cases: Event-driven architecture (e.g., API calls triggering billing updates).

- **Storage:**
  - **S3**: Object storage for storing and retrieving data.
    - Use Cases: Store invoice PDFs, logs, or archived billing data.
  - **EBS**: Block storage for EC2 instances.

- **Database:**
  - **RDS**: Managed relational databases like MySQL or PostgreSQL.
    - Use Cases: Billing database for transactional data.
  - **DynamoDB**: NoSQL database for low-latency, high-throughput needs.
    - Use Cases: Real-time usage tracking.

- **Networking:**
  - **VPC**: Isolated network for securing resources.
  - **API Gateway**: Manage APIs securely with features like rate limiting and caching.

#### **2. AWS Cost Management**
- **Billing Dashboard**: Track and manage AWS costs.
- **Cost Explorer**: Visualize and analyze spending trends.
- **AWS Budgets**: Set alerts for budget limits.

#### **3. Hands-On Practice**
- **Scenario 1**: Design a scalable architecture for a billing system.
  - **Solution**:
    - Use Lambda for generating invoices on an event (e.g., usage data uploaded to S3).
    - Store invoice data in RDS.
    - Cache recent invoices in Redis.

---

Here’s the **complete solution** for the scalable architecture of a billing system based on your scenario. I’ll break it into components and provide practical steps, along with explanations, code snippets, and best practices.

---

### **Scenario 1: Design a Scalable Architecture for a Billing System**

#### **Problem Description**
You need a system that:
1. Generates invoices whenever usage data is uploaded.
2. Stores invoices in a reliable database (RDS).
3. Caches frequently accessed invoices to improve performance (Redis).

---

### **Solution: Scalable Architecture**

1. **Trigger Event**:
   - Use **Amazon S3** to store raw usage data files.
   - An event (e.g., file upload) in S3 triggers **AWS Lambda**.

2. **Invoice Generation**:
   - **AWS Lambda** reads the uploaded usage data, calculates the billing amount, and generates an invoice.

3. **Persistent Storage**:
   - Store invoice details in an **Amazon RDS** instance (e.g., MySQL or PostgreSQL) for reliable, long-term storage.

4. **Caching**:
   - Cache frequently accessed invoices in **Redis** to reduce latency for read operations.

5. **Client Access**:
   - Use an API (e.g., built with Flask) to allow clients to fetch invoice details.

---

### **Implementation Steps**

#### **Step 1: Set Up S3 for Usage Data**
- Create an S3 bucket to store raw usage data (e.g., `usage-data-bucket`).

**S3 Event Trigger**:
- Configure an event trigger for file uploads that invokes the Lambda function.
- Example: JSON for S3 Event:
  ```json
  {
    "Event": "s3:ObjectCreated:*",
    "LambdaFunctionConfigurations": [
      {
        "Id": "InvoiceGeneratorTrigger",
        "LambdaFunctionArn": "arn:aws:lambda:region:account-id:function:GenerateInvoice"
      }
    ]
  }
  ```

---

#### **Step 2: Lambda Function to Generate Invoices**
**Python Lambda Code**:
1. Read the uploaded usage data from S3.
2. Calculate the invoice amount.
3. Store invoice data in RDS and cache it in Redis.

```python
import boto3
import pymysql
import redis
import json

# Initialize AWS and Redis clients
s3 = boto3.client('s3')
rds_host = 'your-rds-endpoint'
redis_client = redis.StrictRedis(host='your-redis-host', port=6379, decode_responses=True)

# Database connection
def connect_to_rds():
    return pymysql.connect(
        host=rds_host,
        user='admin',
        password='password',
        database='billing_db'
    )

def lambda_handler(event, context):
    # Parse S3 event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    # Fetch usage data from S3
    usage_data = s3.get_object(Bucket=bucket_name, Key=object_key)['Body'].read().decode('utf-8')
    usage = json.loads(usage_data)  # Example usage: {"customer_id": 1, "usage_amount": 100}
    
    # Generate invoice
    invoice = {
        "customer_id": usage['customer_id'],
        "amount": usage['usage_amount'] * 0.1,  # Assume $0.1 per unit
        "status": "pending"
    }
    
    # Store in RDS
    conn = connect_to_rds()
    with conn.cursor() as cursor:
        query = """
        INSERT INTO invoices (customer_id, amount, status) VALUES (%s, %s, %s)
        """
        cursor.execute(query, (invoice['customer_id'], invoice['amount'], invoice['status']))
        conn.commit()
    
    # Cache in Redis
    invoice_key = f"invoice:{cursor.lastrowid}"
    redis_client.hmset(invoice_key, invoice)
    redis_client.expire(invoice_key, 3600)  # Cache expires in 1 hour
    
    return {"message": "Invoice generated successfully", "invoice_id": cursor.lastrowid}
```

---

#### **Step 3: Set Up RDS (MySQL)**
**Create Schema for Invoices**:
```sql
CREATE TABLE invoices (
    invoice_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    status ENUM('pending', 'paid') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**RDS Configuration**:
- Choose an instance type (e.g., `db.t3.micro`).
- Enable Multi-AZ for high availability.
- Set up a security group to allow Lambda to connect.

---

#### **Step 4: Set Up Redis**
- Deploy Redis using Amazon ElastiCache or a self-managed instance.
- Configure a security group to allow Lambda access.

**Redis Commands for Caching**:
- **Set an Invoice**:
  ```python
  redis_client.hmset('invoice:123', {'customer_id': 1, 'amount': 100.00, 'status': 'pending'})
  ```
- **Get an Invoice**:
  ```python
  invoice = redis_client.hgetall('invoice:123')
  ```

---

#### **Step 5: Flask API for Client Access**
Expose the data via an API to clients.

**Flask Code**:
```python
from flask import Flask, jsonify
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='your-redis-host', port=6379, decode_responses=True)

@app.route('/invoice/<int:invoice_id>', methods=['GET'])
def get_invoice(invoice_id):
    # Check Redis cache first
    invoice_key = f"invoice:{invoice_id}"
    invoice = redis_client.hgetall(invoice_key)
    
    if invoice:
        return jsonify({"source": "cache", "invoice": invoice})
    
    # Fetch from RDS if not in cache
    # (Assume a function fetch_invoice_from_rds exists to query RDS)
    invoice = fetch_invoice_from_rds(invoice_id)
    if invoice:
        redis_client.hmset(invoice_key, invoice)  # Cache it
        redis_client.expire(invoice_key, 3600)    # Set expiration
    return jsonify({"source": "database", "invoice": invoice})

if __name__ == "__main__":
    app.run(debug=True)
```

---

### **High-Level Architecture Diagram**
1. **S3**:
   - Stores usage data.
   - Triggers Lambda on upload.
2. **Lambda**:
   - Processes usage data.
   - Generates invoices.
   - Saves to RDS and caches in Redis.
3. **Redis**:
   - Caches recent invoices for fast retrieval.
4. **RDS**:
   - Stores all invoices for long-term storage and reporting.
5. **Flask API**:
   - Provides endpoints for fetching invoices.

---

### **Key Benefits**
- **Scalability**: S3 and Lambda handle dynamic loads without pre-provisioning.
- **Performance**: Redis reduces load on RDS by caching recent invoices.
- **Reliability**: RDS ensures data integrity with backups and ACID compliance.

Would you like help setting up any specific component or understanding any step in more detail?


### **Part 2: MySQL Basics**
Relational databases are central to many billing systems.

#### **1. Core Concepts**
- **CRUD Operations**:
  - `INSERT`: Add new billing data.
  - `SELECT`: Retrieve invoices or customer information.
  - `UPDATE`: Modify invoice status (e.g., from pending to paid).
  - `DELETE`: Remove old or test data.
- **Joins**:
  - Combine data across tables (e.g., customers and invoices).
- **Transactions**:
  - Ensure atomic operations using `COMMIT` and `ROLLBACK`.

#### **2. Indexing**
- Use indexes to speed up searches on large datasets.
- Example:
  ```sql
  CREATE INDEX idx_customer_id ON invoices (customer_id);
  ```

#### **3. Normalization**
- Break data into smaller tables to reduce redundancy.
- Example:
  - **Customer Table**: `customer_id`, `name`, `email`.
  - **Invoice Table**: `invoice_id`, `customer_id`, `amount`, `status`.

---

### **4. Practical Scenarios**
#### **Scenario 1: Write a query to fetch overdue invoices**
```sql
SELECT customer_id, SUM(amount) AS total_due 
FROM invoices 
WHERE due_date < CURDATE() 
AND status = 'pending'
GROUP BY customer_id;
```

#### **Scenario 2: Design a table schema for a billing system**
```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE invoices (
    invoice_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    amount DECIMAL(10, 2),
    due_date DATE,
    status ENUM('pending', 'paid', 'overdue'),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

#### **Scenario 3: Update invoice status**
```sql
UPDATE invoices 
SET status = 'paid' 
WHERE invoice_id = 123 AND status = 'pending';
```

---

### **Key Action Plan for Today**
1. **AWS Architecture**:
   - Review core services and design a simple billing system architecture.
2. **MySQL**:
   - Practice CRUD operations and schema design.
   - Optimize queries using indexes.
3. **Hands-On Practice**:
   - Write a query to fetch data from a sample billing table.
   - Design a schema for a billing system.

---

Let me know how you want to proceed or if you need further clarification on any point!

