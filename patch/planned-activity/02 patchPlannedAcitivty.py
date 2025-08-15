import requests
import os
import sys

API_URL = os.getenv("prodURL")
TOKEN = os.getenv("tokenP")

if not API_URL or not TOKEN:
    print("Error: Pastikan environment variable 'API_URL' dan 'TOKEN' sudah di-set.", file=sys.stderr)
    sys.exit(1) # Keluar dengan status error

ids_str = """
264655
264660
264665
264690
264700
264715
264730
264735
264740
264745
264765
264770
264800
264815
264825
264905
264910
264915
264920
264900
264895
264890
264885
264880
264875
264870
264865
264860
264855
264850
264845
264840
264835
264830
264820
264810
264805
264795
264790
264785
264780
264775
264760
264755
264750
264725
264720
264710
264705
264695
264685
264680
264675
264670
264650
264645
264640
264983
264917
264912
264907
264902
264897
264892
264887
264882
264877
264872
264867
264862
264857
264852
264847
264842
264837
264832
264827
264822
264817
264812
264807
264802
264797
264792
264787
264782
264777
264772
264767
264762
264757
264752
264747
264742
264737
264732
264727
264722
264717
264712
264707
264702
264697
264692
264687
264682
264677
264672
264667
264662
264657
264652
264647
264642
264637
264978
264977
264976
264975
264974
264973
264972
264971
264970
264969
264968
264967
264966
264965
264964
264963
264962
264961
264960
264959
264958
264957
264956
264955
264954
264953
264952
264951
264950
264949
264948
264947
264946
264945
264944
264943
264942
264941
264940
264939
264938
264937
264936
264935
264934
264933
264932
264931
264930
264929
264928
264927
264926
264925
264924
264923
264922
264918
264913
264908
264903
264898
264893
264888
264883
264878
264873
264868
264863
264858
264853
264848
264843
264838
264833
264828
264823
264818
264813
264808
264803
264798
264793
264788
264783
264778
264773
264768
264763
264758
264753
264748
264743
264738
264733
264728
264723
264718
264713
264708
264703
264698
264693
264688
264683
264678
264673
264668
264663
264658
264653
264648
264643
264638
264919
264914
264909
264904
264899
264894
264889
264884
264879
264874
264869
264864
264859
264854
264849
264844
264839
264834
264829
264824
264819
264814
264809
264804
264799
264794
264789
264784
264779
264774
264769
264764
264759
264754
264749
264744
264739
264734
264729
264724
264719
264714
264709
264704
264699
264694
264689
264684
264679
264674
264669
264664
264659
264654
264649
264644
264639
"""
# Mengubah string menjadi list of strings, membersihkan spasi kosong
ids = ids_str.strip().split()

# --- Payload untuk dikirim dalam request ---
payload = {
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
        "gpsAccuracyThreshold": 5,
        "stopMeasurementsOutsidePlot": False
    }
}

def main():
    with requests.Session() as s:
        s.headers.update({'Authorization': f'Bearer {TOKEN}'})

        print(f"Memproses {len(ids)} ID...\n")

        for an_id in ids:
            try:
                full_url = f'{API_URL.rstrip("/")}/planned-activity/{an_id}'

                res = s.patch(full_url, json=payload, timeout=15) # Menambahkan timeout

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