import json
import os

acquisition_format = {
    "protected": {
        "ver": "v1",
        "alg": "none",
    },
    "signature": "",
    "payload": {
        "device_type": "FEATHER-ESP32",
        "interval_ms": 5000,
        "sensors": [
            {"name": "thermo", "units": "Cel"},
        ],
        "values": [
        ]
    }
}

j = 0

sample = acquisition_format

for root, dirs, files in os.walk('./data_collection/Data/'):
    for file in files:
        with open(os.path.join(root, file), "r") as file:
            text = file.readlines()
            for index, line in enumerate(text):
                jsonObj = json.loads(line)
                sample['payload']['values'].append([float(jsonObj['Body']['Temperature'])])
                if len(sample['payload']['values']) % 720 == 0:
                    with open(f'sample_{j}.json', 'w') as file:
                        json.dump(sample, file)
                    j += 1
                    sample['payload']['values'].clear()