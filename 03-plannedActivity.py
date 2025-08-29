import os
import requests
import sys
import pandas
import json

# --- Configuration ---
# Get configuration from environment variables.
PROD_AUTH_TOKEN = os.getenv('tokenP')
PROD_API_URL = os.getenv('prodURL')
ENDPOINT_PATH = "/v2/planned-activity/create"
ACTIVITY_TEMPLATE_PATH = "C:/Users/mardi/Repo/LDC-configuration/json/activityTemplate.json"
PLOT_IDS_PATH = "C:/Users/mardi/Repo/LDC-configuration/data/plots.csv"

# --- Data ---
# List of user IDs. Each ID must be on a new line.
USER_IDS = """
18347
18352
"""

def create_payload(user_id, plot_id, template_id, template_config):
    """Creates a dictionary (payload) for the JSON request body."""
    return {
        "type": "adhoc",
        "activityTemplateID": template_id,      # Use the ID from the JSON file
        "configuration": template_config,     # Use the configuration from the JSON file
        "userIds": [int(user_id)],
        "plotIds": [int(plot_id)]
    }


def main():
    """Main function to run the script."""
    # 1. Validate environment variables
    if not PROD_AUTH_TOKEN or not PROD_API_URL:
        print("❌ Error: Make sure the 'tokenP' and 'prodURL' environment variables are set.")
        sys.exit(1)

    # 2. Read and parse the activityTemplate.json file
    try:
        with open(ACTIVITY_TEMPLATE_PATH, 'r', encoding='utf-8') as f:
            activity_template = json.load(f)
        template_id = activity_template.get("id")
        template_config = activity_template.get("configuration")

        if not template_id or not template_config:
            print(f"❌ Error: 'id' or 'configuration' not found in the file '{ACTIVITY_TEMPLATE_PATH}'.")
            sys.exit(1)
        print(f"✅ Successfully loaded data from '{ACTIVITY_TEMPLATE_PATH}'.")

    except FileNotFoundError:
        print(f"❌ Error: File '{ACTIVITY_TEMPLATE_PATH}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"❌ Error: Failed to parse JSON from file '{ACTIVITY_TEMPLATE_PATH}'. Make sure the format is correct.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error while reading the activity template file: {e}")
        sys.exit(1)


    # 3. Combine the base URL with the endpoint
    full_api_url = f"{PROD_API_URL}{ENDPOINT_PATH}"

    # 4. Read Plot IDs from the CSV file using pandas
    try:
        df = pandas.read_csv(PLOT_IDS_PATH)
        if "Plot ID" not in df.columns:
            print(f"❌ Error: The file '{PLOT_IDS_PATH}' does not have a 'Plot ID' column.")
            sys.exit(1)
        # Get all values from the 'Plot ID' column and convert them to a list
        plot_ids_list = df["Plot ID"].tolist()
        print(f"✅ Successfully loaded {len(plot_ids_list)} Plot IDs from the file '{PLOT_IDS_PATH}'.")
    except FileNotFoundError:
        print(f"❌ Error: File '{PLOT_IDS_PATH}' not found. Make sure the file path is correct.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error while reading the CSV file: {e}")
        sys.exit(1)


    # 5. Clean and convert the user ID string into a list
    user_ids_list = USER_IDS.strip().split()

    # 6. Prepare headers for the API request
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': f'Bearer {PROD_AUTH_TOKEN}'
    }

    print(f"\n🚀 Starting the process of creating planned activities at URL: {full_api_url}")

    # 7. Iterate over each plot and user
    for plot_id in plot_ids_list:
        for user_id in user_ids_list:
            # Create the payload for the current combination, using data from the JSON file
            payload = create_payload(user_id, plot_id, template_id, template_config)
            print(f"   -> Sending request for User ID: {user_id}, Plot ID: {plot_id}")

            try:
                # Send a POST request to the complete URL
                response = requests.post(full_api_url, headers=headers, json=payload)

                # Check for HTTP errors (e.g., 401, 404, 500)
                response.raise_for_status()

                print(f"   ✅ Success! Status: {response.status_code}, Response: {response.json()}\n")

            except requests.exceptions.RequestException as e:
                # Display a more informative error
                error_message = f"   ❌ Failed! Error: {e}"
                if e.response:
                    error_message += f"\n      Response Body: {e.response.text}"
                print(f"{error_message}\n")


if __name__ == "__main__":
    main()