# Projeto conecta #
## Hackathon Sebrae 22/09/2019 - Equipe Cavaleiros Tropicanos ##

Este repositório contém 

### Instalação e configuração do ambiente

O sistema foi desenvolvido no MacOS Mojave, 
no entanto deve ser possível também a instalação das ferramentas em outros sistemas operacionais,
em especial no Linux.

O projeto foi desenvolvido em Python 3.7.4 e Nodejs 10.6.3, os quais devem estar previamente instalados.

Recomenda-se o uso do `virtualenv` para isolar as dependências do ambiente Python.

Para instalar as dependências do Python, basta navegar até o diretório raiz do projeto (/hackathon_sebrae):

`pip install -r all_requirements.txt`

Alguns pacotes python dependem da instalação de dependências no Sistema Operacional nativo.

Para a parte do nodejs, em `/hackathon_sebrae/scraper`, digitar:

` $ yarn install `



### Programas desenvolvidos

Todos os programas foram desenvolvidos para uso na linha de comando, não há interface gráfica (poderia existir no futuro). 
Os programas ou scripts em `python` são executados utilizando `python nome_do_programa.py`. Uma mensagem simples de argumentos esperados é saída.
Vamos descrevê-los um a um brevemente.

O web scraper executado em nodejs também pode ser chamado a partir de um script `wrapper` em Python.


##### enrich_with_icms.py
`Usage: enrich_with_icms.py dataset_filepath active_txt cancelled_txt output_directory`
Parâmetros:

dataset_filepath: Caminho para dataset de entrada no formato .csv (fornecido pelo SEBRAE)
active_txt: Caminho para arquivo .txt de registros ativos no ICMS
cancelled_txt: Caminho para arquivo .txt de registros cancelados no ICMS
output_directory: Diretório de saída

#### scrapper_wrapper.py

`Usage: scraper_wrapper.py dataset output_directory [batch_mode]`
Recebe um dataset de entrada em arquivo .csv, no formato fornecido pelo SEBRAE nesta competição,
e aciona o web scraper Puppeteer para buscar os primeiros links fornecidos pelo Duckduckgo, salvando cada resultado em
`.json` no diretório fornecido. A função batch_mode ainda não foi habilitada (trabalhos futuros)

#### json_reader.py
Ainda não utilizado (trabalhos futuros)


