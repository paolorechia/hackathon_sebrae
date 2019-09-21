import os
import sys
import json
import subprocess
import csv
from json_config import JSON_DIRECTORY
from json_config import SHOES_DIRECTORY

FIRST_PAGE_SCRAPER='scraper/duckduck_v2_firstpages_scraper.js';

def scrape_first_pages(DB_DIRECTORY, CNPJ, COMPANY_NAME): 
    output_file = os.path.join(DB_DIRECTORY, CNPJ) + '.json'
    print('Scraping first pages of {} ({})'.format(CNPJ, COMPANY_NAME))
    call_wrapper=['node', FIRST_PAGE_SCRAPER, COMPANY_NAME, output_file]
    print(call_wrapper)
    subprocess.run(['node',FIRST_PAGE_SCRAPER, COMPANY_NAME, output_file],\
                    capture_output=False)

if __name__ == "__main__":
    if len(sys.argv) < 4):
        print('Usage: {} dataset output_directory'.format(sys.argv[0]))
        sys.exit(1)
    output_directory=sys.argv[3]
    output_directory=os.path.join(JSON_DIRECTORY, SHOES_DIRECTORY)

    cnpj=sys.argv[1]
    search_words=sys.argv[2]
#    scrape_first_pages(shoes_json_directory, \
#                       'test', 'CALCADOS RIGONI')
#    scrape_first_pages(shoes_json_directory, \
#                       '21882532000170', '3 FRONTEIRAS CALCADOS')
