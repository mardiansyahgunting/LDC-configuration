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
7888
7889
7890
7891
7892
7893
7894
7895
7896
7897
7898
7899
7900
7901
7902
7903
7904
7905
7906
7907
7908
7909
8331
7910
7911
7912
7913
7914
7915
7916
7917
7918
7919
7920
7921
7922
7923
7924
8376
8019
8024
8025
8026
8027
8028
8029
8030
8031
8032
8033
8034
8035
8036
8037
8078
8079
8080
8081
8082
8083
8084
8085
8086
8087
8088
8379
8089
8090
8091
8092
8380
8093
8094
8095
8096
8382
8097
8098
8099
8100
8101
8102
8116
8117
8118
8119
8120
8121
8122
8123
8124
8125
8126
8127
8128
8129
8130
8131
8132
8133
8134
8135
8136
8137
8138
8139
8140
8141
8142
8383
8152
8153
8384
8154
8155
8156
8386
8157
8158
8159
8225
8226
8227
8228
8229
8230
8231
8232
8233
8234
8235
8236
8237
8238
8239
8240
8241
8242
8243
8244
8245
8252
8282
8338
8283
8325
8284
8285
8286
8287
8288
8289
8290
8291
8292
8293
8337
8377
8378
8381
8385
"""

# Mengubah string menjadi list of strings, membersihkan spasi kosong
ids = ids_str.strip().split()

# --- Payload untuk dikirim dalam request ---
payload = {
    "ownerID": 18352 # ganti ke plot Enumerator yang sesuai
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
