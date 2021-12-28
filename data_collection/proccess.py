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

for root, dirs, files in os.walk('../Data/'):
    for file in files:
        with open(os.path.join(root, file)) as file:
            text = file.readlines()
            # print(text)
            sample = acquisition_format
            samples = []
            for position, line in enumerate(text):
                jsonObj = json.loads(text[position])
                sample['payload']['values'].append([float(jsonObj['Body']['Temperature'])])
                if position % 720 == 0:
                    with open(f'sample_{j}.json', 'w') as file:
                        json.dump(sample, file)
                    j += 1
                    # print(sample)
                    # samples.append(sample)
                    sample['payload']['values'].clear()

for i, sample in enumerate(samples):
    with open(f'sample_{i}.json', 'w') as file:
        json.dump(sample, file)
