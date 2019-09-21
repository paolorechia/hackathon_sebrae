import os
import sys
import json
from json_config import JSON_DIRECTORY

def read_json(DB_DIRECTORY, CNPJ): 
    json_filepath = os.path.join(JSON_DIRECTORY, DB_DIRECTORY, CNPJ + '.json')
    print(json_filepath)
    with open(json_filepath) as json_file:
        data = json.load(json_file)
        print(data)

if __name__ == '__main__':
    read_json('shoes', '21882532000170')
