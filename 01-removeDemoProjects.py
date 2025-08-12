import requests
import os
import time

# Step 1: Get sensitive data from environment variables
# Make sure you have set the 'prodURL' and 'tokenP' variables in your system.
API_URL = os.getenv("prodURL")
TOKEN = os.getenv("tokenP")

# Step 2: Define IDs using a multiline string and .split()
user_rule_ids_string = """
20564
"""
user_rule_ids = user_rule_ids_string.split()

# --- Credentials Check ---
if not API_URL or not TOKEN:
    print("❌ Error: Make sure the environment variables 'prodURL' and 'tokenP' are set.")
    exit()

# Prepare headers once
headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json'  # Common additional header
}

# Changed the description to reflect the GET request method
print("🚀 Starting the request process...")

# --- Request Process ---
for rule_id in user_rule_ids:
    # Skip if the line is empty (a result of .split() on newlines at the start/end)
    if not rule_id.strip():
        continue

    endpoint = f"{API_URL}/user-projects/delete/{rule_id}"

    try:
        # --- MODIFIED THIS LINE ---
        # Changed from requests.delete to requests.get as requested
        res = requests.get(endpoint, headers=headers, timeout=15)

        res.raise_for_status()  # Will raise an error if the status is 4xx or 5xx

        # Adjusted the success message to be more accurate for a GET request
        print(f"✅ Request for ID {rule_id} sent successfully (Status: {res.status_code})")

    except requests.exceptions.HTTPError as err:
        print(
            f"❗ Failed to process ID {rule_id}. Server responded with an error: {err.response.status_code} - {err.response.text}")
    except requests.exceptions.RequestException as err:
        print(f"❗ Failed to process ID {rule_id}. A connection error occurred: {err}")

    # Pause between requests to avoid overloading the server
    time.sleep(0.5)

print("\n✨ Process finished.")