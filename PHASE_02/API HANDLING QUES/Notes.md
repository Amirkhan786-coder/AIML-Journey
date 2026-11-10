# Complete API Handling in Python – Detailed Notes



Beginner to Advanced

B.Tech CS – AI/ML



PHASE 02 — Python for Data & AI/ML Engineering

These notes cover API Handling from absolute basics to advanced concepts, with English definitions, easy Hinglish explanations, diagrams, Python code, practical examples, and interview preparation.

## Complete syllabus

| No. | Topic                          | Level        |
| --- | ------------------------------ | ------------ |
| 1   | Introduction to API            | Basic        |
| 2   | How API Works                  | Basic        |
| 3   | API Terminologies              | Basic        |
| 4   | HTTP and HTTPS                 | Basic        |
| 5   | JSON and XML                   | Basic        |
| 6   | HTTP Methods                   | Basic        |
| 7   | Status Codes                   | Basic        |
| 8   | Python Requests Library        | Basic        |
| 9   | GET Request                    | Basic        |
| 10  | POST Request                   | Basic        |
| 11  | PUT, PATCH, DELETE             | Basic        |
| 12  | Query Parameters               | Intermediate |
| 13  | Headers and Request Body       | Intermediate |
| 14  | Response Handling              | Intermediate |
| 15  | API Authentication             | Intermediate |
| 16  | API Keys and Tokens            | Intermediate |
| 17  | Exception Handling             | Intermediate |
| 18  | Timeout and Retry              | Intermediate |
| 19  | Pagination                     | Intermediate |
| 20  | API Session                    | Intermediate |
| 21  | REST API                       | Intermediate |
| 22  | CRUD Operations                | Intermediate |
| 23  | Rate Limiting                  | Advanced     |
| 24  | Async API Requests             | Advanced     |
| 25  | API Integration with Pandas    | AI/ML        |
| 26  | API Integration with ML Models | AI/ML        |
| 27  | FastAPI                        | Advanced     |
| 28  | API Security                   | Advanced     |
| 29  | API Testing                    | Advanced     |
| 30  | Real-World API Project         | Project      |

# UNIT 01 — Introduction to API

## 1. What is an API?

Definition: API stands for Application Programming Interface. It is a set of rules and protocols that allows two or more software applications to communicate with each other.

Easy Hinglish Explanation:

API ek bridge ki tarah hoti hai jo do different applications ke beech communication karwati hai.

Maan lo tum ek weather application bana rahe ho. Tumhe weather information chahiye, lekin tumhare paas weather ka database nahi hai.

Tum Weather API ko request bhejoge. Weather API tumhe temperature, humidity, wind speed aur weather conditions ka data return karegi.

[MCP vs API: Key Differences, Benefits, and Use Cases](https://images.openai.com/static-rsc-4/ZhVavSyCXTXDbwdTRpFIMSAzRbtYaF5hBEyfgrcJLvPcCfdOFBYhxxUrXKdDTWEDLU3YuysbOO-6jkKDYMX0fbAfQCF7sQj7x16BXSd2QlQGU1f0w1NL22WlWbK_7DZBkelFATEp6mkcMezf1vzSYCkKBZQ28sBIZ5-mCJJl5Ko?purpose=inline)

[upgrad.com](https://www.upgrad.com/blog/mcp-vs-api/?utm_source=chatgpt.com)

### Real-life examples of API

| Application          | API usage                      |
| -------------------- | ------------------------------ |
| Google Maps          | Location and navigation        |
| Weather App          | Temperature and weather        |
| Instagram            | Sharing and retrieving content |
| Payment Gateway      | Online payments                |
| YouTube              | Video and channel information  |
| ChatGPT applications | AI model integration           |

### Why do we use APIs?

1. Data sharing between applications.
2. Connecting frontend and backend.
3. Integrating third-party services.
4. Accessing external databases.
5. Connecting AI/ML models.
6. Automating business processes.
7. Building scalable applications.

## 2. Types of APIs

APIs can be classified according to their access permissions and architecture.

### A. Based on access

1\. Public API

An API available for external developers to use, sometimes with registration or usage restrictions.

Example: Public weather and country-information APIs.

2\. Private API

An API used internally within an organization.

Example: A company's employee management API.

3\. Partner API

An API shared with authorized business partners.

Example: A shipping company sharing tracking services with an e-commerce company.

4\. Composite API

An API that combines multiple operations or services into one interface.

Example: One request retrieves customer, order and payment information.

### B. Based on architecture or communication style

| Type          | Explanation                               |
| ------------- | ----------------------------------------- |
| REST API      | Uses HTTP methods and resource-based URLs |
| SOAP API      | Uses structured XML messaging             |
| GraphQL API   | Allows clients to request specific fields |
| WebSocket API | Supports two-way real-time communication  |
| gRPC API      | Uses efficient remote procedure calls     |

[REST APIs — Beginner Friendly Guide | by Swastik Sharma | Medium](https://images.openai.com/static-rsc-4/0N8vFfZhJwq3eFPXiJ8d_gIP83hhtgaFFEW2AzNXINWE7kEBJmExA4Q41RyAqOK3p0EwMocEr23EkgSdJEZgG48q-xmnKbGDaN-kD4Qyxs-JPpLYKYZrVpP01YYi8V7hkLVXXhvYAlm9_nrR6LVTUYLgvdRx95UoGZgF8hxQxl0?purpose=inline)

[Understanding Graphql Basics: Queries  – peerdh.com](https://images.openai.com/static-rsc-4/JBT-FAf7dOAW-kDagrX_zQRmDHmC9x-0ULY1SYpLIw4Aa2-NomOmnDHEEV9IVILqbQ11dxMYcrgP13UK0_OjDQPhJ81UuMW5PZd5YfLwJ3r-B30CrRsnTigjwFM3elV66UmN9QvExG2J4vUMcrDrRvwfz9BqT3xJn_fCvmwCJXY?purpose=inline)

[PPT - Web Services Introduction and Components Explained PowerPoint Presentation - ID:5625482](https://images.openai.com/static-rsc-4/mLJVqkaTTQOTtFbXS0yijI7Nf8JDyfNqVUTY6w99l-BT9HPUq5tUH-Guvtta18nr0Gj9bcnG_1FPc_QK-VdLq_-bbCDVxmB-ZEBZgWxMrM1WjF4QGyq5bkRhmz_GAcHtUyrmxqp_LhteRzHvdPUdEzwCDT5eUK6UvnFnhowyHkU?purpose=inline)

[Understanding WebSocket Connection (Simple Explanation) - DEV Community](https://images.openai.com/static-rsc-4/AEUs4Kv9X1352-LnOkfnIOZ8sv2wL_KffWwqaini95Wxys7RrQRjp0oWDACFJS12AXpXrrYxXxs-iQgG58d5GvB6x6Xf5lcXLx23h_jLAikZDfDueS1_KmQt8tDKloicGzmt2WcZc_0EKhgpn8H8EFMIMYm8y0dIIKYjEQmmQWI?purpose=inline)

Important: REST, SOAP and GraphQL are not all the same kind of thing. REST is an architectural style, SOAP is a protocol, GraphQL is a query language and runtime, and WebSocket is a communication protocol.

# UNIT 02 — How API Works

## 3. API Request and Response Cycle

Definition: An API request is a message sent by a client to a server to perform an operation or retrieve information.

An API response is the message returned by the server after processing the request.

### Four main components

1. Client – Application that sends a request.
2. Request – Message sent to the server.
3. Server – Processes the request.
4. Response – Result returned to the client.

[What is an API? Complete Beginner's Guide - DEV Community](https://images.openai.com/static-rsc-4/PR4fRS0oX39Fgr3jqQTwjmPkzSRvPNsvTTAY8ZJGWtOkGwDuJQzNZ1WL1I0bHwMgCLA8N12dadvOsBuPYIbUa78PGi_IwQqDT_wMmZt3O4viBacancgyIFiKHFx6hyt4C1rdpktL5bCRDHdY43fmrAR_OKOnBN16EEqqSeilQZw?purpose=inline)

[dev.to](https://dev.to/theodoresummer/what-is-an-api-complete-beginners-guide-2ag8?utm_source=chatgpt.com)

### Example

Suppose you search for a student in a college application.

```
Student Application
        |
        | GET /students/101
        |
        v
    API Server
        |
        | Search student in database
        |
        v
     Database
        |
        | Student information
        |
        v
    API Server
        |
        | JSON Response
        |
        v
Student Application
```

### Sample API response

```
{
    "id": 101,
    "name": "Amir Khan",
    "course": "B.Tech AI-ML",
    "year": 2
}
```

The application receives this data and displays it to the user.

## 4. Important API Terminologies

| Term           | Definition                     | Easy explanation    |
| -------------- | ------------------------------ | ------------------- |
| Client         | Request sender                 | Application         |
| Server         | Request processor              | Backend system      |
| Endpoint       | Specific API address           | Data ka address     |
| URL            | Uniform Resource Locator       | Web address         |
| HTTP           | Communication protocol         | Data exchange rules |
| Request        | Client message                 | Data maangna/bhejna |
| Response       | Server message                 | Data receive karna  |
| Payload        | Data sent in a request         | Actual data         |
| Header         | Additional request information | Extra details       |
| Authentication | Identity verification          | User verification   |
| Authorization  | Permission verification        | Access permission   |
| Token          | Authentication credential      | Access pass         |
| API Key        | API access credential          | Secret key          |
| Latency        | Time taken for response        | Response delay      |
| Rate Limit     | Request usage restriction      | Request ki limit    |

## 5. API Endpoint

Definition: An endpoint is a specific URL through which a client accesses a particular API resource or operation.

Example:

```
https://api.example.com/students
```

Different endpoints:

```
/students
/students/101
/courses
/teachers
```

Explanation:

- `/students` – Access all students.
- `/students/101` – Access student with ID 101.
- `/courses` – Access courses.
- `/teachers` – Access teachers.

## 6. HTTP and HTTPS

HTTP: Hypertext Transfer Protocol is a protocol used for communication between clients and web servers.

HTTPS: Hypertext Transfer Protocol Secure is the secure version of HTTP, using TLS encryption.

| HTTP                                  | HTTPS                          |
| ------------------------------------- | ------------------------------ |
| Communication without TLS encryption  | Communication protected by TLS |
| Less secure for sensitive information | Protects data in transit       |
| Uses `http://`                        | Uses `https://`                |
| Generally port 80                     | Generally port 443             |

Example:

```
http://example.com
https://example.com
```

Always prefer HTTPS when working with API credentials or sensitive information.

# UNIT 03 — JSON and XML

## 7. What is JSON?

Definition: JSON stands for JavaScript Object Notation. It is a lightweight text-based format used to store and exchange structured data.

Hinglish: JSON ek format hai jisme API data ko key-value pairs ke form mein send aur receive karti hai.

Example:

```
{
    "name": "Amir",
    "age": 20,
    "course": "AI-ML",
    "skills": ["Python", "SQL", "NumPy"],
    "is_student": true
}
```

### JSON data types

| Data type | Example            |
| --------- | ------------------ |
| String    | `"Amir"`           |
| Number    | `20`               |
| Boolean   | `true`             |
| Null      | `null`             |
| Array     | `[10, 20, 30]`     |
| Object    | `{"name": "Amir"}` |

### Important JSON rules

1. Keys must be strings enclosed in double quotes.
2. String values use double quotes.
3. Numbers do not require quotation marks.
4. Boolean values are `true` or `false`.
5. Null is written as `null`.
6. Trailing commas are not allowed.

## 8. JSON vs Python Dictionary

| JSON                   | Python Dictionary                 |
| ---------------------- | --------------------------------- |
| Data exchange format   | Python data structure             |
| `true`                 | `True`                            |
| `false`                | `False`                           |
| `null`                 | `None`                            |
| Double-quoted strings  | Single or double quotes           |
| Used for communication | Used for Python data manipulation |

### Convert Dictionary into JSON

```
import jsonstudent = {    "name": "Amir",    "age": 20,    "course": "AI-ML"}json_data = json.dumps(student, indent=4)print(json_data)
```

### Convert JSON into Dictionary

```
import jsonjson_data = '{"name": "Amir", "age": 20}'student = json.loads(json_data)print(student["name"])print(student["age"])
```

### Important JSON functions

| Function       | Purpose                      |
| -------------- | ---------------------------- |
| `json.dumps()` | Python object to JSON string |
| `json.loads()` | JSON string to Python object |
| `json.dump()`  | Write JSON to file           |
| `json.load()`  | Read JSON from file          |

## 9. What is XML?

Definition: XML stands for Extensible Markup Language. It is a markup language used to store and transport structured data.

Example:

```
<student>
    <name>Amir</name>
    <age>20</age>
    <course>AI-ML</course>
</student>
```

### JSON vs XML

| JSON                  | XML                     |
| --------------------- | ----------------------- |
| Lightweight           | More verbose            |
| Key-value structure   | Tag-based structure     |
| Easy to use in Python | Requires XML parsing    |
| Common in REST APIs   | Common in SOAP services |

# UNIT 04 — HTTP Methods

## 10. What are HTTP Methods?

Definition: HTTP methods specify the action that a client wants to perform on a resource.

There are five essential methods.

[How to Use OpenAPI Specification for Effective API Testing?](https://images.openai.com/static-rsc-4/gjU61LvMa5SG2xKM9OXerOSixIIraXo-QdgYxiSW-DEg1molnTAma5fvf99Gb3ecUsWZUrkvWwI5efXVHbR9ubzfgitWtW89pRct8yQGovMX3l6pqN-2dpPwC-bnBwPE5gYWLhLNfjxiuCGqdQJrMW0hcdNuV4veRoPGnRjc8tM?purpose=inline)

[frugaltesting.com](https://www.frugaltesting.com/blog/how-to-use-openapi-specification-for-effective-api-testing?utm_source=chatgpt.com)

### A. GET Method

Definition: GET is used to retrieve data from a server.

Example:

```
GET /students
```

Python:

```
import requestsurl = "https://jsonplaceholder.typicode.com/users"response = requests.get(url)print(response.status_code)print(response.json())
```

### B. POST Method

Definition: POST is commonly used to submit data to a server and create a new resource.

```
import requestsurl = "https://jsonplaceholder.typicode.com/posts"data = {    "title": "Python API",    "body": "Learning API",    "userId": 1}response = requests.post(url, json=data)print(response.status_code)print(response.json())
```

### C. PUT Method

Definition: PUT is generally used to replace the state of a resource with the supplied representation.

```
import requestsurl = "https://jsonplaceholder.typicode.com/posts/1"data = {    "id": 1,    "title": "Updated Title",    "body": "Updated Content",    "userId": 1}response = requests.put(url, json=data)print(response.status_code)print(response.json())
```

### D. PATCH Method

Definition: PATCH is used to partially update an existing resource.

```
import requestsurl = "https://jsonplaceholder.typicode.com/posts/1"data = {    "title": "New Title"}response = requests.patch(url, json=data)print(response.status_code)print(response.json())
```

### E. DELETE Method

Definition: DELETE is used to request deletion of a specified resource.

```
import requestsurl = "https://jsonplaceholder.typicode.com/posts/1"response = requests.delete(url)print(response.status_code)
```

### Difference between HTTP Methods

| Method | Operation      | Idempotent?     |
| ------ | -------------- | --------------- |
| GET    | Read           | Yes             |
| POST   | Create/submit  | Generally no    |
| PUT    | Replace        | Yes             |
| PATCH  | Partial update | Not necessarily |
| DELETE | Delete         | Yes             |

Idempotent meaning: Repeating the same request has the same intended effect as making it once.

# UNIT 05 — HTTP Status Codes

## 11. What are Status Codes?

Definition: HTTP status codes are three-digit numbers returned by a server to indicate the result of a client's request.

### 1xx – Informational

| Code | Meaning             |
| ---- | ------------------- |
| 100  | Continue            |
| 101  | Switching Protocols |

### 2xx – Success

| Code | Meaning    |
| ---- | ---------- |
| 200  | OK         |
| 201  | Created    |
| 202  | Accepted   |
| 204  | No Content |

### 3xx – Redirection

| Code | Meaning           |
| ---- | ----------------- |
| 301  | Moved Permanently |
| 302  | Found             |
| 304  | Not Modified      |

### 4xx – Client Errors

| Code | Meaning               |
| ---- | --------------------- |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Not Found             |
| 405  | Method Not Allowed    |
| 408  | Request Timeout       |
| 409  | Conflict              |
| 422  | Unprocessable Content |
| 429  | Too Many Requests     |

### 5xx – Server Errors

| Code | Meaning               |
| ---- | --------------------- |
| 500  | Internal Server Error |
| 501  | Not Implemented       |
| 502  | Bad Gateway           |
| 503  | Service Unavailable   |
| 504  | Gateway Timeout       |

### Python example

```
import requestsurl = "https://jsonplaceholder.typicode.com/users"response = requests.get(url)if response.status_code == 200:    print("Request Successful")elif response.status_code == 404:    print("Data Not Found")elif response.status_code >= 500:    print("Server Error")else:    print("Status:", response.status_code)
```

# UNIT 06 — Python Requests Library

## 12. What is Requests?

Definition: Requests is a third-party Python library used to send HTTP requests and interact with web APIs.

Installation:

```
pip install requests
```

Import:

```
import requests
```

### Important Requests functions

| Function             | Purpose                   |
| -------------------- | ------------------------- |
| `requests.get()`     | Send GET request          |
| `requests.post()`    | Send POST request         |
| `requests.put()`     | Send PUT request          |
| `requests.patch()`   | Send PATCH request        |
| `requests.delete()`  | Send DELETE request       |
| `requests.request()` | Send a custom HTTP method |
| `requests.Session()` | Create a session          |

### Basic GET request

```
import requestsurl = "https://jsonplaceholder.typicode.com/users"response = requests.get(url)print(response)
```

Expected output:

```
<Response [200]>
```

### Response object properties

| Property               | Purpose                     |
| ---------------------- | --------------------------- |
| `response.status_code` | HTTP status                 |
| `response.url`         | Requested URL               |
| `response.text`        | Response text               |
| `response.content`     | Raw response bytes          |
| `response.headers`     | Response headers            |
| `response.encoding`    | Response encoding           |
| `response.ok`          | Whether status is below 400 |
| `response.history`     | Redirect history            |

### Response methods

```
response.json()response.raise_for_status()response.close()
```

`response.json()` parses JSON into Python objects. It does not itself confirm that the HTTP request succeeded.

# UNIT 07 — GET Request in Detail

## 13. Fetch all records

```
import requestsurl = "https://jsonplaceholder.typicode.com/users"response = requests.get(url)response.raise_for_status()users = response.json()for user in users:    print(user["name"])
```

## 14. Fetch one record

```
import requestsurl = "https://jsonplaceholder.typicode.com/users/1"response = requests.get(url)response.raise_for_status()user = response.json()print("Name:", user["name"])print("Email:", user["email"])
```

## 15. Query Parameters

Definition: Query parameters are key-value pairs added to a URL to filter or customize an API request.

Example:

```
https://api.example.com/students?course=AI-ML&year=2
```

Python:

```
import requestsurl = "https://jsonplaceholder.typicode.com/posts"params = {    "userId": 1}response = requests.get(url, params=params)print(response.url)print(response.json())
```

Multiple parameters:

```
params = {    "userId": 1,    "id": 2}
```

## 16. Path Parameters vs Query Parameters

| Path Parameter        | Query Parameter             |
| --------------------- | --------------------------- |
| Identifies a resource | Filters or modifies results |
| Part of URL path      | Appears after `?`           |
| `/users/10`           | `/users?city=Delhi`         |

# UNIT 08 — POST, PUT, PATCH and DELETE in Detail

## 17. POST Request with JSON Data

Definition: POST sends data to a server, commonly to create a new resource.

Example: Registering a new student.

```
import requestsurl = "https://jsonplaceholder.typicode.com/posts"student = {    "name": "Amir Khan",    "course": "B.Tech AI-ML",    "year": 2}response = requests.post(    url,    json=student,    timeout=10)print("Status:", response.status_code)print("Response:", response.json())
```

### Important parameters

- `url`: API endpoint.
- `json`: Data sent as JSON.
- `timeout`: Maximum waiting time for the request operation.

## 18. JSON vs Data Parameters in POST

Requests supports two common ways of sending request data.

Using `json=`

```
response = requests.post(    url,    json={"name": "Amir"})
```

This sends JSON and automatically sets the JSON content type.

Using `data=`

```
response = requests.post(    url,    data={"name": "Amir"})
```

This sends form-encoded data by default when given a dictionary.

Use `json=` when the API expects a JSON request body and `data=` when it expects form data or raw body content.

## 19. PUT vs PATCH

PUT: Usually replaces the complete resource representation.

PATCH: Updates selected fields of a resource.

Example:

```
import requestsurl = "https://jsonplaceholder.typicode.com/posts/1"# PUTput_data = {    "title": "Python",    "body": "API Learning",    "userId": 1}put_response = requests.put(url, json=put_data)# PATCHpatch_data = {    "title": "Advanced Python"}patch_response = requests.patch(url, json=patch_data)print(put_response.json())print(patch_response.json())
```

## 20. DELETE Request

```
import requestsurl = "https://jsonplaceholder.typicode.com/posts/1"response = requests.delete(url)if response.status_code in (200, 202, 204):    print("Delete request successful")else:    print("Status:", response.status_code)
```

Important: Successful DELETE requests may return 200, 202 or 204 depending on the API. Do not assume every API returns the same status code.

# UNIT 09 — API Headers and Request Body

## 21. What are HTTP Headers?

Definition: HTTP headers are additional metadata sent with requests and responses to provide information about communication.

Hinglish: Headers server ko batate hain ki request kis type ki hai, authentication kya hai aur response kis format mein chahiye.

Example:

```
import requestsurl = "https://jsonplaceholder.typicode.com/users"headers = {    "Accept": "application/json",    "User-Agent": "Python Application"}response = requests.get(url, headers=headers)print(response.status_code)
```

### Common HTTP Headers

| Header          | Meaning                     |
| --------------- | --------------------------- |
| Accept          | Expected response format    |
| Content-Type    | Request body format         |
| Authorization   | Authentication information  |
| User-Agent      | Client identification       |
| Cache-Control   | Caching instructions        |
| Accept-Language | Preferred response language |

### Content-Type examples

```
application/json
application/xml
application/x-www-form-urlencoded
multipart/form-data
text/plain
```

## 22. What is a Request Body?

Definition: A request body contains the actual data sent from the client to the server.

Example:

```
{
    "name": "Amir",
    "email": "amir@example.com"
}
```

In Python:

```
import requestsurl = "https://jsonplaceholder.typicode.com/posts"payload = {    "title": "My First API",    "body": "Learning Python API Handling",    "userId": 1}response = requests.post(url, json=payload)print(response.json())
```

Request body is commonly used with POST, PUT and PATCH.

# UNIT 10 — API Authentication

## 23. What is Authentication?

Definition: Authentication is the process of verifying the identity of a user or application before allowing access to protected resources.

Example: Login system.

```
Username + Password
        |
        v
 Authentication Server
        |
        v
 Identity Verification
        |
        v
 Access Granted / Denied
```

## 24. Types of API Authentication

### A. API Key Authentication

An API key is a unique credential used to identify an application or authorize API access.

```
import requestsurl = "https://api.example.com/data"api_key = "YOUR_API_KEY"headers = {    "X-API-Key": api_key}response = requests.get(    url,    headers=headers,    timeout=10)print(response.status_code)
```

Some APIs expect the key as a query parameter or a differently named header. Always check API documentation.

### B. Bearer Token Authentication

A Bearer token is a credential sent in the Authorization header.

```
import requestsurl = "https://api.example.com/profile"token = "YOUR_ACCESS_TOKEN"headers = {    "Authorization": f"Bearer {token}"}response = requests.get(url, headers=headers)print(response.status_code)
```

### C. Basic Authentication

Basic Authentication sends a username and password encoded in Base64.

```
import requestsurl = "https://api.example.com/data"response = requests.get(    url,    auth=("username", "password"),    timeout=10)print(response.status_code)
```

Base64 encoding is not encryption. Always use HTTPS.

### D. OAuth 2.0

Definition: OAuth 2.0 is an authorization framework that allows applications to access protected resources using tokens.

Example: Allowing an application to access Google services after user authorization.

Typical flow:

```
User
 |
 v
Application
 |
 v
Authorization Server
 |
 v
Access Token
 |
 v
Protected API
 |
 v
Data Response
```

OAuth 2.0 is widely used in modern applications.

## 25. Environment Variables and API Key Security

Never hardcode secret API keys in public source code.

Install:

```
pip install python-dotenv
```

Create `.env`:

```
API_KEY=your_secret_key
```

Python:

```
import osfrom dotenv import load_dotenvload_dotenv()api_key = os.getenv("API_KEY")if not api_key:    raise ValueError("API key not found")print("API key loaded successfully")
```

Add this to `.gitignore`:

```
.env
```

Security rule: Never print, commit or share API keys, passwords or access tokens.

# UNIT 11 — Exception Handling in API

## 26. What is API Exception Handling?

Definition: Exception handling is the process of detecting and managing errors that occur during API communication.

Why is it important?

- Internet may disconnect.
- API server may be unavailable.
- URL may be incorrect.
- Authentication may fail.
- Request may take too long.
- Response may contain invalid JSON.

### Common Requests exceptions

| Exception          | Meaning                                  |
| ------------------ | ---------------------------------------- |
| `Timeout`          | Request exceeded its timeout             |
| `ConnectionError`  | Connection problem                       |
| `HTTPError`        | Unsuccessful HTTP response after raising |
| `InvalidURL`       | Invalid URL                              |
| `JSONDecodeError`  | Invalid JSON response                    |
| `RequestException` | General Requests exception               |

### Complete example

```
import requestsurl = "https://jsonplaceholder.typicode.com/users"try:    response = requests.get(url, timeout=10)    response.raise_for_status()    data = response.json()    for user in data:        print(user["name"])except requests.exceptions.Timeout:    print("Server took too long to respond")except requests.exceptions.ConnectionError:    print("Check your internet connection")except requests.exceptions.HTTPError as error:    print("HTTP Error:", error)except requests.exceptions.RequestException as error:    print("Request Error:", error)except ValueError:    print("Invalid JSON response")
```

### Important difference

`try` – Contains code that might cause an error.

`except` – Handles the error.

`else` – Executes if no exception occurs.

`finally` – Executes whether an exception occurs or not.

Example:

```
try:    print("API Request Started")except Exception as e:    print("Error:", e)else:    print("Request completed without exception")finally:    print("Program Finished")
```

# UNIT 12 — Timeout, Retry and Rate Limiting

## 27. API Timeout

Definition: Timeout specifies how long a client waits for a network operation before stopping that operation.

Example:

```
import requestsurl = "https://jsonplaceholder.typicode.com/users"response = requests.get(url, timeout=5)print(response.json())
```

Here, `timeout=5` sets a five-second timeout for the connection and read operations (not a strict total execution deadline).

## 28. Retry Mechanism

Definition: Retry is the process of attempting a failed API request again.

Why use retry?

- Temporary network problems.
- Server overload.
- Temporary service unavailability.
- Rate limiting.

Simple retry:

```
import requestsimport timeurl = "https://jsonplaceholder.typicode.com/users"for attempt in range(3):    try:        response = requests.get(url, timeout=5)        response.raise_for_status()        print(response.json())        break    except requests.exceptions.RequestException as error:        print("Attempt:", attempt + 1)        print("Error:", error)        if attempt < 2:            time.sleep(2)
```

### Exponential Backoff

Definition: Exponential backoff is a retry strategy in which the waiting time increases after each failed attempt.

Example:

```
Attempt 1 → Wait 1 second
Attempt 2 → Wait 2 seconds
Attempt 3 → Wait 4 seconds
Attempt 4 → Wait 8 seconds
```

This reduces unnecessary requests to an overloaded server.

## 29. Rate Limiting

Definition: Rate limiting restricts how many requests a client can make within a specific time period.

Example:

```
100 requests per minute
```

If the client exceeds the limit, the server may return:

```
429 Too Many Requests
```

Some APIs provide a `Retry-After` header to tell the client how long to wait.

Python:

```
import requestsurl = "https://api.example.com/data"response = requests.get(url, timeout=10)if response.status_code == 429:    wait_time = response.headers.get("Retry-After")    print("Too many requests")    print("Retry after:", wait_time)else:    print(response.status_code)
```

# UNIT 13 — Pagination and API Session

## 30. API Pagination

Definition: Pagination is a technique of dividing large amounts of API data into smaller pages.

Why is pagination needed?

Suppose a college database contains 50,000 students. Sending all records in one response can consume memory and increase response time.

Instead, the API returns records in smaller batches.

[Pagination - by Franco Fernando - The Polymathic Engineer](https://images.openai.com/static-rsc-4/Zxg7q1fgFYyPUwLH_H_3Xv8u4ct80yGsjanZqconc1v5fZOgbqvczwy-Lv46-dfVqMjdS3Dgi60Y4uzEQJb6lxOsbOj22nmx96DI-2dLaYy1jBR24gSz0LLwA03N47tyfBtGbkLJFma2y2F_VxuNmwkEQXuAGG9Xz5Y7cXV3r_8?purpose=inline)

[newsletter.francofernando.com](https://newsletter.francofernando.com/p/pagination?utm_source=chatgpt.com)

Example URL:

```
https://api.example.com/students?page=1&limit=10
```

Python:

```
import requestsurl = "https://api.example.com/students"params = {    "page": 1,    "limit": 10}response = requests.get(url, params=params)print(response.json())
```

### Common pagination types

| Type         | Explanation                    |
| ------------ | ------------------------------ |
| Page-based   | Uses page number               |
| Offset-based | Uses offset and limit          |
| Cursor-based | Uses next cursor               |
| Link-based   | Uses next-page URL in response |

### Page-based example

```
import requestsurl = "https://api.example.com/students"for page in range(1, 4):    params = {        "page": page,        "limit": 10    }    response = requests.get(url, params=params, timeout=10)    response.raise_for_status()    data = response.json()    print("Page:", page)    print(data)
```

This is a conceptual example. The actual parameter names and response structure depend on the API.

## 31. API Session

Definition: A Session object allows multiple requests to share certain settings, cookies and connections.

Why use sessions?

1. Reuse connections.
2. Maintain cookies.
3. Reuse headers.
4. Reduce repeated configuration.

Example:

```
import requestssession = requests.Session()session.headers.update({    "Accept": "application/json"})try:    response = session.get(        "https://jsonplaceholder.typicode.com/users",        timeout=10    )    response.raise_for_status()    print(response.json())finally:    session.close()
```

# UNIT 14 — REST API and CRUD Operations

## 32. What is REST API?

Definition: REST stands for Representational State Transfer. It is an architectural style for designing network-based applications.

REST APIs commonly use HTTP methods to perform operations on resources.

### Important REST principles

1. Client-Server Architecture
2. Stateless Communication
3. Cacheability
4. Uniform Interface
5. Layered System
6. Code on Demand (optional)

### Statelessness

Definition: Each request should contain the information necessary to process it, without relying on stored client session state on the server.

Example:

Every protected request can carry its own access token.

## 33. CRUD Operations

CRUD stands for:

- Create
- Read
- Update
- Delete

These are the four fundamental data operations.

| CRUD   | HTTP Method | Example        |
| ------ | ----------- | -------------- |
| Create | POST        | Add student    |
| Read   | GET         | Fetch student  |
| Update | PUT/PATCH   | Update student |
| Delete | DELETE      | Remove student |

### Example REST API structure

```
GET     /students
GET     /students/101
POST    /students
PUT     /students/101
PATCH   /students/101
DELETE  /students/101
```

### REST API best practices

- Use nouns for resource names.
- Use appropriate HTTP methods.
- Return correct status codes.
- Keep request and response formats consistent.
- Use HTTPS.
- Validate user input.
- Document API endpoints.
- Version APIs when necessary.

Example of versioning:

```
/api/v1/students
/api/v2/students
```

# UNIT 15 — Advanced API Concepts

## 34. Synchronous vs Asynchronous API Requests

Synchronous: A program waits for one operation to finish before continuing with the next operation.

Asynchronous: A program can perform other tasks while waiting for an I/O operation to complete.

### Synchronous example

```
import requestsurls = [    "https://jsonplaceholder.typicode.com/users",    "https://jsonplaceholder.typicode.com/posts"]for url in urls:    response = requests.get(url, timeout=10)    response.raise_for_status()    print(response.status_code)
```

### Asynchronous example using aiohttp

Install:

```
pip install aiohttp
```

Code:

```
import asyncioimport aiohttpasync def fetch(session, url):    async with session.get(url) as response:        response.raise_for_status()        return await response.json()async def main():    urls = [        "https://jsonplaceholder.typicode.com/users",        "https://jsonplaceholder.typicode.com/posts"    ]    timeout = aiohttp.ClientTimeout(total=10)    async with aiohttp.ClientSession(timeout=timeout) as session:        tasks = [            fetch(session, url)            for url in urls        ]        results = await asyncio.gather(*tasks)        for result in results:            print(result)asyncio.run(main())
```

### Difference

| Synchronous                 | Asynchronous                    |
| --------------------------- | ------------------------------- |
| Blocking execution          | Non-blocking I/O approach       |
| Easier for beginners        | Requires async concepts         |
| Requests library            | aiohttp or HTTPX                |
| Suitable for simple scripts | Useful for concurrent I/O tasks |

## 35. API Caching

Definition: API caching stores previously retrieved responses temporarily to avoid unnecessary repeated requests.

Example:

```
First Request → API Server → Response
Second Request → Cache → Response
```

Benefits:

- Faster response.
- Less network traffic.
- Reduced server load.
- Better performance.

Caching may be handled using HTTP cache headers, application caches or caching services.

## 36. Webhooks

Definition: A webhook is an HTTP callback mechanism where one application sends a request to another application's URL when a particular event occurs.

Example: Payment successful.

```
Customer makes payment
          |
          v
Payment Gateway
          |
          v
Payment Successful
          |
          v
Webhook Notification
          |
          v
Your Application
```

Difference:

| API Polling                             | Webhook                                        |
| --------------------------------------- | ---------------------------------------------- |
| Application repeatedly asks for updates | Server sends event notification                |
| Repeated requests                       | Event-driven                                   |
| May cause unnecessary traffic           | Usually more efficient for event notifications |

Important: Webhooks should verify signatures and avoid trusting arbitrary incoming requests.

# UNIT 16 — API Integration with Python Data Science Libraries

## 37. API + NumPy

Definition: API integration with NumPy means fetching numerical data from an API and processing it using NumPy arrays and mathematical operations.

Example: Fetch numerical data.

```
import requestsimport numpy as npurl = "https://jsonplaceholder.typicode.com/posts"response = requests.get(url, timeout=10)response.raise_for_status()data = response.json()ids = np.array([item["id"] for item in data])print("IDs:", ids)print("Mean:", np.mean(ids))print("Maximum:", np.max(ids))print("Minimum:", np.min(ids))
```

Applications:

- Numerical analysis.
- Statistical calculations.
- Scientific computing.
- Data preprocessing.

## 38. API + Pandas

Definition: API and Pandas integration allows developers to retrieve external data and manipulate it using DataFrames.

[Simple Steps Towards Data Processing - by kiran kumar](https://images.openai.com/static-rsc-4/y-KR6N8t91uUhx-0llEeF80KGYWPm3Euvf3vOfuHocXbhUaRorYIn-WuG0WCnQ8oksSfA4qmG0BX_OoStN-gbUUVWVz0p2E0DP1msXBhP4sHw2HIy0_NkSnZc7eMz2CInlvLQL6bDMLlqAAHT1MffFHVpAu9-tQiZZ405GpWfAk?purpose=inline)

[newsletter.kirankbs.com](https://newsletter.kirankbs.com/p/simple-steps-towards-data-processing?utm_source=chatgpt.com)

Example:

```
import requestsimport pandas as pdurl = "https://jsonplaceholder.typicode.com/users"response = requests.get(url, timeout=10)response.raise_for_status()data = response.json()df = pd.DataFrame(data)print(df.head())print(df.info())print(df.isnull().sum())print(df.describe(include="all"))
```

### Select specific columns

```
print(df[["name", "email"]])
```

### Filter records

```
filtered = df[df["id"] > 5]print(filtered)
```

### Save data

```
df.to_csv("api_data.csv", index=False)
```

## 39. API + Matplotlib

Definition: API and Matplotlib integration allows developers to visualize data retrieved from external APIs.

Example:

```
import requestsimport matplotlib.pyplot as plturl = "https://jsonplaceholder.typicode.com/posts"response = requests.get(url, timeout=10)response.raise_for_status()data = response.json()ids = [item["id"] for item in data[:10]]plt.plot(ids, marker="o")plt.title("API Data Visualization")plt.xlabel("Record Number")plt.ylabel("Post ID")plt.show()
```

## 40. API + Machine Learning

Definition: API integration with Machine Learning allows applications to retrieve external data, preprocess it and use trained ML models to generate predictions.

### Example workflow

[Simple Machine Learning Model Deployment using FastAPI | by Faisal Malik Widya Prasetya | Medium](https://images.openai.com/static-rsc-4/-ZM6A52gaKkU5mWAIoxO_Z5pI3I8MQ61-CXsHyUIb7GZyDQ8UR-jJiWF7DrWcYJ4BYm5SSKctw-K_2KIxoRFJ1HqLL8oT8OSHt5Nwb-S0c0PXOoriMidvikgivVj2I3vTfeQTa6fzwu8_KeJk3aFF-dTD3Gchxv9xEF1Pr4G28c?purpose=inline)

[faisalmalikwp.medium.com](https://faisalmalikwp.medium.com/simple-machine-learning-model-deployment-using-fastapi-5a6388db985f?utm_source=chatgpt.com)

1. Fetch data from an external API.
2. Convert JSON into Python data.
3. Perform data cleaning.
4. Apply feature engineering.
5. Pass features to the trained ML model.
6. Generate predictions.
7. Return results through an API.

### Example code structure

```
import requestsimport pandas as pdurl = "https://jsonplaceholder.typicode.com/users"response = requests.get(url, timeout=10)response.raise_for_status()data = response.json()df = pd.DataFrame(data)print("Data fetched:", df.shape)print(df.head())
```

This example fetches and processes data. Actual ML predictions require a compatible trained model and the correct model input features.

### Real-world AI/ML applications

| Project                        | API Usage                             |
| ------------------------------ | ------------------------------------- |
| AI Resume Analyzer             | Resume analysis and model integration |
| Weather Prediction             | Weather data retrieval                |
| Stock Analysis                 | Financial market data                 |
| Chatbot                        | AI model API integration              |
| Recommendation System          | Product and user data                 |
| Student Performance Prediction | Student data integration              |

# UNIT 17 — FastAPI: Building Your Own API

## 41. What is FastAPI?

Definition: FastAPI is a modern Python web framework used to build APIs with automatic validation, documentation and support for asynchronous programming.

Important distinction:

- `requests` is used to consume existing APIs.
- `FastAPI` is used to build your own APIs.

[APIs Without Tears: A Gentle Intro to FastAPI | by chaithanya k | Medium](https://images.openai.com/static-rsc-4/3cktEMypu2oPgJ5HJPd3SxpPZSW0RqMUPlGIfj8KWbibJuUDIkdOTUqg2kr1THVfXk6Q797-1GfSh-p5RB_U47HYf4IcZLCO-Un1f8CQaaXwg5mGxuBJZ1k_OB82lHAzd45Is5zH0LRWY6_NSF7Oa1ZgLGHYHhSASO7URz2JSMM?purpose=inline)

[medium.com](https://medium.com/%40cchaithanya83/apis-without-tears-a-gentle-intro-to-fastapi-ba3667a10bd3?utm_source=chatgpt.com)

### Why FastAPI?

1. Easy to learn.
2. High performance.
3. Automatic API documentation.
4. Data validation.
5. Type hints support.
6. Asynchronous support.
7. Useful for ML model deployment.

## 42. Install FastAPI

```
pip install fastapi uvicorn
```

## 43. Create Your First API

Create a file named:

```
main.py
```

Python code:

```
from fastapi import FastAPIapp = FastAPI()@app.get("/")def home():    return {        "message": "Welcome to My First API",        "student": "Amir",        "course": "AI-ML"    }
```

Run the application:

```
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

Expected response:

```
{
    "message": "Welcome to My First API",
    "student": "Amir",
    "course": "AI-ML"
}
```

## 44. FastAPI GET Endpoint

```
from fastapi import FastAPIapp = FastAPI()students = [    {"id": 1, "name": "Amir"},    {"id": 2, "name": "Rahul"},    {"id": 3, "name": "Aman"}]@app.get("/students")def get_students():    return students
```

Open:

```
http://127.0.0.1:8000/students
```

## 45. FastAPI POST Endpoint

```
from fastapi import FastAPIfrom pydantic import BaseModelapp = FastAPI()class Student(BaseModel):    name: str    age: int    course: str@app.post("/students")def create_student(student: Student):    return {        "message": "Student Created Successfully",        "data": student    }
```

FastAPI uses Pydantic models to validate request data.

## 46. Automatic API Documentation

FastAPI provides interactive documentation automatically.

[image](https://www.google.com/s2/favicons?domain=https://swagger.io\&sz=32)

Swagger UI

Interactive API testing

[Open /docs](http://127.0.0.1:8000/docs?utm_source=chatgpt.com)

ReDoc

API reference documentation

[Open /redoc](http://127.0.0.1:8000/redoc?utm_source=chatgpt.com)

These local links work after starting your FastAPI server.

# UNIT 18 — API Security

## 47. What is API Security?

Definition: API security refers to the practices used to protect APIs from unauthorized access, misuse and attacks.

### Important security concepts

| Concept                  | Explanation                         |
| ------------------------ | ----------------------------------- |
| Authentication           | Verify identity                     |
| Authorization            | Verify permissions                  |
| HTTPS                    | Encrypt data in transit             |
| API Key Security         | Protect secret credentials          |
| Input Validation         | Check incoming data                 |
| Rate Limiting            | Prevent excessive requests          |
| CORS                     | Control browser cross-origin access |
| SQL Injection Prevention | Protect database queries            |
| Token Expiration         | Limit token lifetime                |

### Common API security risks

1. Exposed API keys.
2. Weak authentication.
3. Broken access control.
4. SQL injection.
5. Excessive API requests.
6. Sensitive information exposure.
7. Improper input validation.

### Best practices

- Always use HTTPS.
- Store secrets in environment variables.
- Validate all input data.
- Use strong authentication.
- Apply role-based authorization.
- Set appropriate rate limits.
- Avoid returning unnecessary sensitive data.
- Keep dependencies updated.
- Verify webhook signatures.

# UNIT 19 — API Testing and Debugging

## 48. What is API Testing?

Definition: API testing is the process of verifying whether an API works correctly according to its expected functionality, performance and security requirements.

### Common API testing tools

[Visionco | services](https://images.openai.com/static-rsc-4/bDTDp-kPgMFGVhrV9CFYRBVY_fSLVnXtPoOpKhXLI7R_6Dwzy0vZ9Fy3dm60OSheomIpV9xh6oPBr_3yHRbF-nji9QjXWEQTk6IwrM2RFuYXFIVNtmk21msDsgCUnZAnB1dL215LsGFTPjnE9Ru9RMPG12V05n6oicPO-am4NKI?purpose=inline)

Postman

Send GET, POST, PUT and DELETE requests and inspect responses.

[Official website](https://www.postman.com/?utm_source=chatgpt.com)

[Swagger Logo PNG Vector (SVG) Free Download](https://images.openai.com/static-rsc-4/DZMUKSvrP0DxUSnLmIuFJy_oanGakoT1xYpFcjU_0p0hhZvGKh6oQXi3K_gtjtDcLqmkv8Rz1kgpG-MCvVGXB4SyxYmt-ebmmKnjCK6iwmLkrtaEX8jfyhiI_cA9-w0YaQHvII5MM3ACSbn4H_0S7VUQFBH_Cyzgv4xpMCIM-js?purpose=inline)

Swagger

Document and interactively test APIs.

[Official website](https://swagger.io/?utm_source=chatgpt.com)

[File:Pytest logo.svg - Wikimedia Commons](https://images.openai.com/static-rsc-4/HAbymyVnhv5o_ebIXc4fnTb7BKnDLOAg3IrHBMGLugeZsZ_DD95aCJk4cpoukhHgjWexEl-IOVbGA5l3qKyXdAj0qMQXNlCzY74ZBmVs5WPSVuHPR36dWmFW_-eW8gEefy3f3SVBx_uRc8c7yqGtSO9oWud3HFuw-W6-Eoy29bk?purpose=inline)

pytest

Write automated Python tests.

[Official website](https://pytest.org/?utm_source=chatgpt.com)

## 49. API Testing with Python

Install:

```
pip install pytest requests
```

Create a file named:

```
test_api.py
```

Code:

```
import requestsdef test_get_users():    url = "https://jsonplaceholder.typicode.com/users"    response = requests.get(url, timeout=10)    assert response.status_code == 200    data = response.json()    assert isinstance(data, list)    assert len(data) > 0def test_single_user():    url = "https://jsonplaceholder.typicode.com/users/1"    response = requests.get(url, timeout=10)    assert response.status_code == 200    data = response.json()    assert data["id"] == 1
```

Run:

```
pytest -v
```

Expected: Both tests should pass when the API is available.

# UNIT 20 — Real-World API Project

## 50. Project: Weather Information System

Beginner to Intermediate Project

Objective: Build a Python application that retrieves real-time weather information using an external weather API.

[Weather Dashboard - Dark mode by Micsaela on Dribbble](https://images.openai.com/static-rsc-4/2PZlXKbY704uJ6MVUfJ_AiNZYbUSvC1Zs5-0O8g7-oocqBzWxTh1CcJLeFXZjsimFVCLBci03TqHYdubPPakttljQXOe7HjmllmwQAdbXecJMugj349gYaW98-Y1m1uXdxAIY8vi9jY7LaoUnqKflXclAWimyrJ4UkQvLB6CSzU?purpose=inline)

[dribbble.com](https://dribbble.com/shots/20787521-Weather-Dashboard-Dark-mode?utm_source=chatgpt.com)

### Features

1. Search weather by city.
2. Display temperature.
3. Display humidity.
4. Display wind speed.
5. Display weather conditions.
6. Handle invalid city names.
7. Handle network errors.
8. Store weather results in CSV.

### Folder structure

```
Weather_API_Project/
│
├── main.py
├── api_handler.py
├── data_handler.py
├── .env
├── .gitignore
│
└── requirements.txt
```

### Step 1: Install libraries

```
pip install requests pandas python-dotenv
```

### Step 2: Create `.env`

```
WEATHER_API_KEY=your_api_key
```

Get an API key from a weather API provider such as OpenWeather.

[OpenWeather API documentation](https://openweathermap.org/api?utm_source=chatgpt.com)

### Step 3: Create api_handler.py

```
import requestsimport osfrom dotenv import load_dotenvload_dotenv()API_KEY = os.getenv("WEATHER_API_KEY")def get_weather(city):    url = "https://api.openweathermap.org/data/2.5/weather"    params = {        "q": city,        "appid": API_KEY,        "units": "metric"    }    try:        response = requests.get(            url,            params=params,            timeout=10        )        response.raise_for_status()        return response.json()    except requests.exceptions.RequestException as e:        print("API Error:", e)        return None
```

### Step 4: Create data_handler.py

```
import pandas as pddef save_weather(data):    record = {        "City": data["name"],        "Temperature": data["main"]["temp"],        "Humidity": data["main"]["humidity"],        "Wind Speed": data["wind"]["speed"]    }    df = pd.DataFrame([record])    df.to_csv(        "weather_data.csv",        mode="a",        header=False,        index=False    )    print("Weather data saved!")
```

### Step 5: Create main.py

```
from api_handler import get_weatherfrom data_handler import save_weathercity = input("Enter City Name: ")data = get_weather(city)if data:    print("\n===== WEATHER REPORT =====")    print("City:", data["name"])    print("Temperature:",          data["main"]["temp"], "°C")    print("Humidity:",          data["main"]["humidity"], "%")    print("Wind Speed:",          data["wind"]["speed"])    print("Weather:",          data["weather"][0]["description"])    save_weather(data)
```

### Step 6: Run

```
python main.py
```

Example input:

```
Enter City Name: Delhi
```

The application will retrieve current weather data if the API key and network are working.

Note: For a production version, add CSV headers when creating the file, validate the city input, handle API error responses, and avoid saving duplicate records unintentionally.

# UNIT 21 — Important API Interview Questions

## 51. Theory Questions

1. What is an API?
2. What is the difference between API and REST API?
3. Explain client-server architecture.
4. What is an API endpoint?
5. What is HTTP and HTTPS?
6. What is JSON?
7. What is the difference between JSON and XML?
8. Explain GET and POST methods.
9. What is the difference between PUT and PATCH?
10. What are HTTP status codes?
11. What is API authentication?
12. What is an API key?
13. What is a Bearer token?
14. What is OAuth 2.0?
15. What is API pagination?
16. What is rate limiting?
17. What is API caching?
18. What is a webhook?
19. What is the difference between synchronous and asynchronous requests?
20. What is FastAPI?

## 52. Practical Interview Questions

Practice writing code for:

1. Fetch data using GET.
2. Fetch a specific user using ID.
3. Send data using POST.
4. Update data using PUT.
5. Update selected fields using PATCH.
6. Delete a record using DELETE.
7. Convert JSON into Python Dictionary.
8. Extract nested JSON data.
9. Handle API exceptions.
10. Add request headers.
11. Implement timeout and retry.
12. Fetch API data into Pandas.
13. Save API data into CSV.
14. Create a REST API using FastAPI.
15. Connect a trained ML model to an API.

# UNIT 22 — Final Revision Sheet

# API Handling Quick Revision

Important concepts to remember before exams and interviews

HTTP Methods

```
GET     = Read
POST    = Create
PUT     = Replace / Update
PATCH   = Partial Update
DELETE  = Delete
```

Status Codes

```
200 = OK
201 = Created
204 = No Content
400 = Bad Request
401 = Unauthorized
403 = Forbidden
404 = Not Found
429 = Too Many Requests
500 = Server Error
```

Important Python Functions

```
requests.get()requests.post()requests.put()requests.patch()requests.delete()response.json()response.textresponse.status_coderesponse.raise_for_status()requests.Session()requests.get(url, timeout=10)
```

Data Science Integration

```
API → JSON → Python Dictionary
    → Pandas DataFrame
    → Data Cleaning
    → Data Analysis
    → Visualization
    → Machine Learning
```

API Development

```
FastAPI
Uvicorn
Pydantic
REST API
Swagger Documentation
```

# UNIT 23 — Your API Handling Completion Roadmap

For your AI/ML engineering journey, follow this learning order:

| Phase | Topics                            | Suggested time |
| ----- | --------------------------------- | -------------- |
| 1     | API Fundamentals, JSON, HTTP      | 1 day          |
| 2     | GET, POST, PUT, PATCH, DELETE     | 1 day          |
| 3     | Requests, Headers, Parameters     | 1 day          |
| 4     | Authentication, Exceptions, Retry | 1 day          |
| 5     | REST, Pagination, Sessions        | 1 day          |
| 6     | API + Pandas + NumPy              | 1 day          |
| 7     | FastAPI + ML Integration          | 2 days         |
| 8     | Weather API Project               | 1–2 days       |

Final Learning Target

By the end of API Handling, you should be able to:

- Understand how APIs communicate.
- Consume external APIs using Python.
- Work with JSON and nested data.
- Handle HTTP methods and status codes.
- Securely manage API keys and tokens.
- Handle errors, timeouts and retries.
- Integrate APIs with NumPy and Pandas.
- Build REST APIs using FastAPI.
- Connect an ML model to a backend API.

Important distinction: API consumption (using `requests`) and API development (using FastAPI) are two separate skills. Learn both.

