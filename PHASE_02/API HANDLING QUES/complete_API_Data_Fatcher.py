import requests

def fetch_user(user_id):

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    try:

        response = requests.get(url, timeout=10)

        response.raise_for_status()

        user = response.json()

        if not user:
            print("User not found!")
            return

        print("\n===== USER DETAILS =====")

        print("ID:", user["id"])
        print("Name:", user["name"])
        print("Username:", user["username"])
        print("Email:", user["email"])
        print("Phone:", user["phone"])
        print("Website:", user["website"])
        print("City:", user["address"]["city"])

    except requests.exceptions.HTTPError:
        print("User not found or HTTP error!")

    except requests.exceptions.RequestException as e:
        print("Connection Error:", e)


while True:

    print("\n===== API DATA FETCHER =====")

    print("1. Search User")
    print("2. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        user_id = input("Enter User ID (1-10): ")

        if user_id.isdigit() and 1 <= int(user_id) <= 10:
            fetch_user(int(user_id))
        else:
            print("Please enter a valid ID from 1 to 10.")

    elif choice == "2":

        print("Thank You!")
        break

    else:
        print("Invalid Choice!")