import requests
import os
import sys

API_URL = os.getenv("prodURL")
TOKEN = os.getenv("tokenP")

if not API_URL or not TOKEN:
    print("Error: Pastikan environment variable 'API_URL' dan 'TOKEN' sudah di-set.", file=sys.stderr)
    sys.exit(1)  # Keluar dengan status error

# plot_ID
ids_str = """
8301
8302
8303
8304
8340
8341
8300
8305
8306
8307
8308
8309
8310
8311
7966
7967
7968
7969
7970
7971
8312
7973
7974
7975
7976
7977
7978
7979
7980
8313
8006
8007
8314
8008
8009
8010
8011
8012
8013
8014
8015
8016
8103
8104
8105
8106
8107
8108
8315
8151
8316
8317
8318
8204
8205
8206
8207
8208
8209
8210
8213
8214
8250
8332
8263
8264
8265
8266
8267
8324
8339
8322
8296
8297
8298
8299
8319
8320
8321
8323
"""

# Mengubah string menjadi list of strings, membersihkan spasi kosong
ids = ids_str.strip().split()

# --- Payload untuk dikirim dalam request ---
payload = {
    "ownerID": 18350 # ganti ke plot Enumerator yang sesuai
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
