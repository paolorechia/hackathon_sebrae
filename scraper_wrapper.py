import os
import sys
import json
import subprocess
import csv
from json_config import JSON_DIRECTORY

FIRST_PAGE_SCRAPER='scraper/duckduck_v2_firstpages_scraper.js';

def scrape_first_pages(DB_DIRECTORY, CNPJ, COMPANY_NAME): 
    output_file = os.path.join(DB_DIRECTORY, CNPJ) + '.json'
    print('Scraping first pages of {} ({})'.format(CNPJ, COMPANY_NAME))
    call_wrapper=['node', FIRST_PAGE_SCRAPER, COMPANY_NAME, output_file]
    print(call_wrapper)
    subprocess.run(['node',FIRST_PAGE_SCRAPER, COMPANY_NAME, output_file],\
                    capture_output=False)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: {} dataset output_directory [batch_mode]'\
            .format(sys.argv[0]))
        sys.exit(1)

    dataset_filepath=sys.argv[1]
    output_directory=sys.argv[2]
    if len(sys.argv) > 3:
        batch_mode=sys.argv[3]

    search_phrase_list = []
    with open(dataset_filepath) as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';')
        header = next(csvreader)
        # for row in csvreader:
        for row in csvreader:
            CNPJ = row['CPF_CNPJ']
            social = row['Razão Social']
            name = row['Nome Fantasia']
            city = row['Cidade']
            neighborhood = row['Bairro']
            address = row['Endereço']
            social = social.strip().replace('EIRELI', '')
            if name.strip() == '-':
                name = social
            name_words = name.split(' ')
            last_word = name_words[len(name_words) - 1]
            name_words_minus_last = name_words[:-1]
            valid_word = False
            for char in last_word:
               if not char.isdigit():
                    valid_word = True
            if valid_word:
                final_name = name
            else:
                final_name = ' '.join(name_words_minus_last)
            search_phrase='{} {}'.format(final_name, city)
#            search_phrase='{} {} {}'.format(final_name, city , neighborhood)
            search_phrase_list.append([CNPJ, search_phrase])

    existing_files =  os.listdir(output_directory)
    downloaded = {}
    for file_ in existing_files:
        downloaded[file_]= True

    if len(sys.argv) > 3 and batch_mode:
        print('Running in batch_mode')
        with open('tmp_batch_mode_scraper.txt', 'w') as batch_scraper_file:
            batch_scraper_file
            for cnpj, phrase in search_phrase_list:
                output_filename = cnpj + '.json'
                if output_filename not in downloaded:
                    scrape_first_pages(output_directory, cnpj, phrase)
                    batch_scraper_file.write(output_filename, ';##;', phrase)
                else:
                    print('Skipping {}'.format(downloaded))
        
    for cnpj, phrase in search_phrase_list:
        print(cnpj, phrase)
        output_filename = cnpj + '.json'
        if output_filename not in downloaded:
            scrape_first_pages(output_directory, cnpj, phrase)
        else:
            print('Skipping {}'.format(downloaded))
#        scrape_first_pages(C)
#    scrape_first_pages(shoes_json_directory, \
#                       'test', 'CALCADOS RIGONI')
#    scrape_first_pages(shoes_json_directory, \
#                       '21882532000170', '3 FRONTEIRAS CALCADOS')
