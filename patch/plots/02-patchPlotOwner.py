import requests
import os
import sys

API_URL = os.getenv("prodURL")
TOKEN = os.getenv("tokenP")

if not API_URL or not TOKEN:
    print("Error: Pastikan environment variable 'API_URL' dan 'TOKEN' sudah di-set.", file=sys.stderr)
    sys.exit(1)  # Keluar dengan status error

ids_str = """
8300
"""
# Mengubah string menjadi list of strings, membersihkan spasi kosong
ids = ids_str.strip().split()

# --- Payload untuk dikirim dalam request ---
payload = {
    "ownerID": 18348
}


def main():
    with requests.Session() as s:
        s.headers.update({'Authorization': f'Bearer {TOKEN}'})

        print(f"Memproses {len(ids)} ID...\n")

        for an_id in ids:
            try:
                full_url = f'{API_URL.rstrip("/")}/plots/v2/{an_id}'

                res = s.patch(full_url, json=payload, timeout=15)  # Menambahkan timeout

                res.raise_for_status()

                print(f"✅ ID: {an_id} | Sukses | Status: {res.status_code}")

            except requests.exceptions.HTTPError as e:
                print(f"❌ ID: {an_id} | Gagal | Status: {e.response.status_code} | Pesan: {e.response.text}")
            except requests.exceptions.RequestException as e:
                print(f"❌ ID: {an_id} | Gagal | Error Koneksi: {e}")
            except Exception as e:
                print(f"❌ ID: {an_id} | Gagal | Terjadi error tak terduga: {e}")


if __name__ == "__main__":
    main()
