import os
import tempfile
import argparse
import json
from json import JSONDecodeError

storage_path = os.path.join(tempfile.geettempdir(), 'storage.data')

parser = argparse.ArgumentParser()
parser.add_argument('--key', dest='key')
parser.add_argument('--value', dest='value')
args = parser.parse_args()
key = args.key
value = args.value

json_data = {}
if os.path.exists(storage_path):
    with open(storage_path, 'r') as infile:
        try:
            json_data = json.load(infile)
        except JSONDecodeError:
            pass
if value:
    json_data.setdefault(key, []).append(value)
    with open(storage_path, 'w') as outfile:
        json.dump(outfile, json_data)
else:
    result = json_data.get(key, [])
    print(', '.join(result))
