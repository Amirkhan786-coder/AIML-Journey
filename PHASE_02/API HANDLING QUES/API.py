print("1. Install and import Requests")
print("pip install requests")
import requests


print("\n2. GET Request – Fetch API Data :\nFetch all users from an API.")
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response.status_code)
print(response.json())


print("\n3. Fetch Specific User Data")
import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

data = response.json()

print("Name:", data["name"])
print("Email:", data["email"])
print("City:", data["address"]["city"])

print("\n4. Fetch All Users Using For Loop")
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

users = response.json()

for user in users:
    print("ID:", user["id"])
    print("Name:", user["name"])
    print("Email:", user["email"])
    print("------------------")

print("\n5. GET Request with Parameters")
import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1
}

response = requests.get(url, params=params)

data = response.json()

for post in data:
    print(post["title"])


print("\n6. POST Request – Send Data")
import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Python API",
    "body": "Learning API Handling",
    "userId": 1
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.json())

print("\n7. PUT Request – Update Complete Data")
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

data = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated Python Content",
    "userId": 1
}

response = requests.put(url, json=data)

print(response.status_code)
print(response.json())


print("\n8. PATCH Request – Update Specific Data")
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

data = {
    "title": "New Updated Title"
}

response = requests.patch(url, json=data)

print(response.status_code)
print(response.json())


print("\n9. DELETE Request")
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.delete(url)

print("Status:", response.status_code)
print("Deleted successfully!")


print("\n10. JSON Handling")
#Convert Python Dictionary into JSON and JSON into Python Dictionary.
import json

student = {
    "name": "Amir",
    "age": 20,
    "course": "AI-ML"
}

# Python Dictionary to JSON
json_data = json.dumps(student, indent=4)

print(json_data)

# JSON to Python Dictionary
python_data = json.loads(json_data)

print(python_data["name"])


print("\n11. API Headers")
import requests

url = "https://jsonplaceholder.typicode.com/users"

headers = {
    "Accept": "application/json",
    "User-Agent": "Python API Client"
}

response = requests.get(url, headers=headers)

print(response.json())


print("\n12. API Authentication – API Key")
#Example structure for an API that uses Bearer token authentication:
import requests

url = "https://api.example.com/data"

api_key = "YOUR_API_KEY"

headers = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(
    url,
    headers=headers,
    timeout=10
)

print(response.json())


print("\n13. Exception Handling")
import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=10)

    response.raise_for_status()

    data = response.json()

    print(data)

except requests.exceptions.Timeout:
    print("Request Timeout!")

except requests.exceptions.ConnectionError:
    print("Internet Connection Error!")

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

except requests.exceptions.RequestException as e:
    print("API Error:", e)


print("\n14. API Data into Pandas DataFrame")
print("pip install pandas requests")
import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url, timeout=10)

response.raise_for_status()

data = response.json()

df = pd.DataFrame(data)

print(df.head())

print("\nColumns:")
print(df.columns)

print("\nShape:")
print(df.shape)


print("\n15. Save API Data into CSV")
import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url, timeout=10)

response.raise_for_status()

data = response.json()

df = pd.DataFrame(data)

df.to_csv("users.csv", index=False)

print("Data saved successfully!")



print("\n16. API Timeout and Retry")
import requests
import time

url = "https://jsonplaceholder.typicode.com/users"

for attempt in range(3):

    try:
        response = requests.get(url, timeout=5)

        response.raise_for_status()

        print(response.json())

        break

    except requests.exceptions.RequestException as e:

        print("Attempt:", attempt + 1)
        print("Error:", e)

        if attempt < 2:
            time.sleep(2)



print("\n17. API Session")
import requests

session = requests.Session()

session.headers.update({
    "Accept": "application/json"
})

try:
    response = session.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=10
    )

    response.raise_for_status()

    print(response.json())

finally:
    session.close()