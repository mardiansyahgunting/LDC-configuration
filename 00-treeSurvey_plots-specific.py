import os
import requests
import sys

# --- Konfigurasi ---
# Mengambil konfigurasi dari environment variables.
# Pastikan Anda sudah mengatur variabel ini di sistem Anda.
# Nama variabel diubah agar lebih jelas dan konsisten.
AUTH_TOKEN = os.getenv('tokenP')
API_URL_BASE = os.getenv('prodURL')
ENDPOINT_PATH = "/v2/planned-activity/create"

# --- Data ---
# Daftar ID pengguna dan plot. Setiap ID harus berada di baris baru.
USER_IDS = """
18349
"""

PLOT_IDS = """
7925
7926
7927
8376
7928
7929
7930
7931
7932
7933
7934
7935
7936
7937
7938
7939
7940
7941
7942
7943
7944
7945
7946
7947
7948
8017
8018
8019
8020
8021
8022
8023
8379
8380
8382
8370
8383
8384
8386
8317
8318
8371
8372
8373
8374
8375
8324
8325
8322
8319
8320
8321
8323
8377
8378
8381
8385
"""


def create_payload(user_id, plot_id):
    """Membuat dictionary (payload) untuk body permintaan JSON."""
    return {
        "type": "adhoc",
        "activityTemplateID": 276,
        "configuration": {
            "manualDBH": "hidden",
            "treeHealth": "required",
            "treeComment": "optional",
            "imageQuality": 90,
            "manualHeight": "hidden",
            "specie_codes": [
                "artocarpus_heterophyllus",
                "areca_catechu",
                "parkia_speciosa_kettering",
                "persea_americana_kettering",
                "archidendron_pauciflorum_kettering",
                "durio_zibethinus_kettering"
            ],
            "addTreeSpecies": False,
            "imageResolution": 1000,
            "groundCoverRequired": False,
            "gpsAccuracyThreshold": 10,
            "stopMeasurementsOutsidePlot": False
        },
        "userIds": [int(user_id)],
        "plotIds": [int(plot_id)]
    }


def main():
    """Fungsi utama untuk menjalankan skrip."""
    # 1. Validasi environment variables
    if not AUTH_TOKEN or not API_URL_BASE:
        print("❌ Error: Pastikan environment variable PROD_AUTH_TOKEN dan PROD_API_URL sudah diatur.")
        sys.exit(1)

    # 2. Menggabungkan URL dasar dengan endpoint
    full_api_url = f"{API_URL_BASE}{ENDPOINT_PATH}"

    # 3. Membersihkan dan mengubah string ID menjadi list
    plot_ids_list = PLOT_IDS.strip().split()
    user_ids_list = USER_IDS.strip().split()

    # 4. Menyiapkan headers untuk permintaan API
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': f'Bearer {AUTH_TOKEN}'
    }

    print(f"🚀 Memulai proses pembuatan planned activity ke URL: {full_api_url}")

    # 5. Melakukan iterasi untuk setiap plot dan user
    for plot_id in plot_ids_list:
        for user_id in user_ids_list:
            # Membuat payload untuk kombinasi saat ini
            payload = create_payload(user_id, plot_id)
            print(f"   -> Mengirim permintaan untuk User ID: {user_id}, Plot ID: {plot_id}")

            try:
                # Mengirim permintaan POST ke URL yang sudah lengkap
                response = requests.post(full_api_url, headers=headers, json=payload)

                # Memeriksa apakah ada error HTTP (spt: 401, 404, 500)
                response.raise_for_status()

                print(f"   ✅ Berhasil! Status: {response.status_code}, Response: {response.json()}\n")

            except requests.exceptions.RequestException as e:
                # Menampilkan error yang lebih informatif
                error_message = f"   ❌ Gagal! Error: {e}"
                if e.response:
                    error_message += f"\n      Response Body: {e.response.text}"
                print(f"{error_message}\n")


if __name__ == "__main__":
    main()
