# -*- coding: utf-8 -*-
import os
import sys
import json
import subprocess
import csv
from json_config import JSON_DIRECTORY

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print('Usage: {} dataset_filepath active_txt cancelled_txt output_directory'.format(sys.argv[0]))
        sys.exit(1)

    dataset_filepath=sys.argv[1]
    active_txt=sys.argv[2]
    cancelled_txt=sys.argv[3]
    output_directory=sys.argv[4]

    active = {}
    habilited = {}
    print(active_txt)
    with open(active_txt, 'r') as active_file:
        for row in active_file:
            columns = row.split(';')
            cnpj = columns[1].lstrip('0')
            active[cnpj]=True 
            habilited[cnpj]= columns[2]

    
    cancelled = {}
    cancellation_date = {}
    with open(cancelled_txt, 'r') as cancelled_file:
        for row in cancelled_file:
            columns = row.split(';')
            cnpj = columns[1].lstrip('0')
            cancelled[cnpj]=True 
            cancellation_date[cnpj]= columns[2]

    if '9006315000110' not in cancellation_date:
        print('uh oh')
        sys.exit(1)
    print(len(cancellation_date.keys()))

    enriched_name = 'icms_enriched_' + \
        dataset_filepath.split('/')[len(dataset_filepath.split('/')) - 1]

    enriched_output = os.path.join(output_directory, enriched_name)
    with open(dataset_filepath, 'r') as input_csvfile:
        with open(enriched_output, 'w') as output_csvfile:
            csvreader = csv.DictReader(input_csvfile, delimiter=';')
            header = next(csvreader)
            print(header)
            output_header = header
            output_header['Situação no ICMS'] = ''
            output_header['Data de Cancelamento no ICMS'] = ''
            writer = csv.DictWriter(output_csvfile, fieldnames=output_header)
            writer.writeheader()
            for row in csvreader:
                cnpj =  row['CPF_CNPJ']
                try:
                    is_active = active[cnpj]
                except KeyError:
                    is_active = False
                try:
                    is_cancelled = cancelled[cnpj]
                except KeyError:
                    is_cancelled = False
                icms_status = '' 
                cancel_date = ''
                icms_status = 'Registro Não Encontrado'
                if is_cancelled and is_active:
                    icms_status = 'Inconsistente'
                    cancel_date = cancellation_date[cnpj]
                elif is_cancelled:
                    icms_status = 'Cancelado'
                    cancel_date = cancellation_date[cnpj]
                elif is_active:
                    icms_status = 'Ativo'
                output_row = row
                output_row['Situação no ICMS']=icms_status
                output_row['Data de Cancelamento no ICMS']=cancel_date
                writer.writerow(output_row)

