import json
import os

input_folder = "output/fhir"
output_file = "synthea_bulk.ndjson"

with open(output_file, 'w') as outfile:
    for filename in os.listdir(input_folder):
        if filename.endswith(".json"):
            with open(os.path.join(input_folder, filename), 'r') as f:
                resource = json.load(f)
                outfile.write(json.dumps(resource) + '\n')

print(f"NDJSON file created: {output_file}")
