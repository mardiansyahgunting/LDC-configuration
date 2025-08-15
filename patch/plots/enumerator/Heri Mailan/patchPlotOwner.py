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
8330
7925
7926
7927
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
7972
7981
7982
7983
7984
7985
7986
7991
7992
7993
7994
7995
7996
7997
7998
7999
8000
8001
8002
8003
8004
8005
8063
8064
8065
8066
8067
8068
8069
8070
8071
8072
8073
8074
8075
8076
8077
8109
8110
8111
8112
8113
8114
8115
8143
8144
8145
8146
8147
8148
8149
8150
8199
8200
8201
8202
8203
8211
8212
8246
8247
8248
8249
8251
8253
8254
8255
8256
8257
8258
8259
8260
8261
8262
8333
8334
8335
8326
8327
8328
8294
8295
8329
8336
"""

# Mengubah string menjadi list of strings, membersihkan spasi kosong
ids = ids_str.strip().split()

# --- Payload untuk dikirim dalam request ---
payload = {
    "ownerID": 18349 # ganti ke plot Enumerator yang sesuai
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
