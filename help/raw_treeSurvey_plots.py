import requests
import json

auth_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Ik1hcmRpYW5zeWFoLkd1bnRpbmcxNDc1IiwiZW1haWwiOiJtYXJkaWFuc3lhaEB0cmVlby5vbmUiLCJpZCI6MTM2MCwiaWF0IjoxNzU0NTM1MDQ4LCJleHAiOjE3NTcxNjUwNDh9.St2GZolVfXpt0QTMhtnJsXKv63PfV47sZfeYArFbxiU'

user_ids = """
18348
18350
18352
18347
1360
"""

plot_ids = """
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

plot_ids = plot_ids.split()
user_ids = user_ids.split()


def json_body(user_id, plot_id):
    return {
        "type": "adhoc",
        "activityTemplateID": 302,
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


for p in plot_ids:
    for u in user_ids:
        the_json_body = json_body(u, p)
        res = requests.post('https://api.treeo.org/v2/planned-activity/create',
                            data=json.dumps(the_json_body),
                            headers={'Content-Type': 'application/json; charset=utf-8',
                                     'Authorization': 'Bearer ' + auth_token})
        print(res.status_code, " ", res.text, "\n\n")
