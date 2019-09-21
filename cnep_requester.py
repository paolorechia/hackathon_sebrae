import os
import sys
import json
import csv
import requests

# curl -X GET --header 'Accept: application/json' 'http://www.transparencia.gov.br/api-de-dados/ceis?codigoSancionado=21882532000170&pagina=1'
# curl -X GET --header 'Accept: application/json' 'http://www.transparencia.gov.br/api-de-dados/cnep?cnpjSancionado=21882532000170&pagina=1'

def get_cnep_request(cnpj):
    response = requests.get(
             'http://www.transparencia.gov.br/api-de-dados/cnep?cnpjSancionado={}&pagina=1'\
                .format(cnpj),
            headers={'Accept': 'application/json'}
        )
    return response.json(), response.status_code 

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: {} input_dataset output_directory'.format(sys.argv[0]))
        sys.exit(1)

    input_filepath = sys.argv[1]
    output_directory = sys.argv[2]

    cnpj_list = []
    with open(input_filepath) as input_file:
        input_csvreader = csv.DictReader(input_file, delimiter=';')
        input_header = next(input_csvreader)
        for row in input_csvreader:
            CNPJ = row['CPF_CNPJ'].strip()
            cnpj_list.append(CNPJ)
            
    existing_files =  os.listdir(output_directory)
    downloaded = {}
    for file_ in existing_files:
        downloaded[file_]= True

    print(cnpj_list)
    for cnpj in cnpj_list:
        print(cnpj)
        output_filename = cnpj + '_cnep_response.json'
        if output_filename not in downloaded:
            try:
                response_json, status_code = get_cnep_request(cnpj)
                to_save_dict = {
                        'response': response_json,
                        'status_code': status_code
                    }
                output_fp = os.path.join(output_directory, output_filename)
                print(output_fp, to_save_dict, status_code)
                with open(output_fp, 'w') as outfile:
                    json.dump(to_save_dict, outfile)
            except Exception as excp:
                print(excp)
                pass
        else:
            print('Skipping request for... {}'.format(downloaded))

