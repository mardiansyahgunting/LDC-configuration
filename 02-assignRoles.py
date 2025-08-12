import requests
import json
import os

# 1. Mengambil nilai dari environment variables
API_URL = os.getenv("prodURL")
auth_token = os.getenv("tokenP")

# 2. Pengecekan untuk memastikan variabel ada
if not API_URL or not auth_token:
    print("❌ Error: Pastikan environment variable 'prodURL' dan 'tokenP' sudah di-set dengan benar.")
    exit()  # Keluar dari skrip jika variabel tidak ditemukan

print(f"✅ Berhasil memuat API URL dari environment variable.")

# --- Data User dan Project ---
user_ids_str = """
18349
"""

project_ids_str = """
117
"""

user_ids = user_ids_str.strip().split()
project_ids = project_ids_str.strip().split()

# --- Headers untuk Request ---
headers = {
    'Content-Type': 'application/json; charset=utf-8',
    'Authorization': f'Bearer {auth_token}'
}

# --- Proses Looping untuk Assignment ---
for project_id in project_ids:
    for user_id in user_ids:
        payload = {
            "projectID": int(project_id),
            "userID": int(user_id),
            "roleID": 205

        }

        # administrator = 204
        # Forester = 205

        try:
            print(f"🚀 Mencoba assign User ID: {user_id} ke Project ID: {project_id}...")

            res = requests.post(
                f'{API_URL}/user-projects',
                data=json.dumps(payload),
                headers=headers
            )

            print(f"-> Status: {res.status_code}, Response: {res.text}\n")

        except requests.exceptions.RequestException as e:
            print(f"Terjadi error saat request: {e}\n")

print("✨ Proses assignment selesai.")