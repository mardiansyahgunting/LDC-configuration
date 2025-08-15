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
8342
8343
8344
8345
8363
8346
8347
8348
8349
8350
8353
8365
8354
8366
8355
7949
7950
7951
8367
7952
8356
7953
7954
7955
7956
7957
7958
7959
7960
7961
7962
7963
7964
7965
8357
8358
7987
7988
7989
7990
8359
8360
8017
8018
8020
8021
8022
8023
8368
8038
8039
8040
8041
8042
8043
8044
8045
8046
8047
8048
8049
8050
8051
8052
8053
8054
8055
8056
8057
8058
8059
8060
8061
8062
8361
8369
8370
8160
8161
8162
8163
8164
8165
8166
8167
8168
8169
8170
8171
8172
8173
8174
8175
8176
8371
8177
8178
8179
8180
8181
8182
8183
8184
8185
8186
8187
8188
8372
8189
8190
8191
8192
8193
8194
8195
8196
8197
8198
8373
8215
8216
8217
8218
8219
8220
8221
8223
8222
8374
8224
8375
8362
8268
8270
8269
8271
8272
8273
8274
8275
8276
8277
8278
8279
8280
8281
8351
8352
8364
"""

# Mengubah string menjadi list of strings, membersihkan spasi kosong
ids = ids_str.strip().split()

# --- Payload untuk dikirim dalam request ---
payload = {
    "ownerID": 18347 # ganti ke plot Enumerator yang sesuai
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
